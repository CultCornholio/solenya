from datetime import datetime
from asyncio import gather

from msph.app import Command, current_app

from ...clients import ms_online as client
from ...exceptions import CliAppError
from .validators import CliValidator, target_names
from ...models import Target, WspTarget, Wsp
from . import msgs
from ... import settings
from ...validators import ClientIdRequired

target = Command('target', __name__,
    validators=[CliValidator(), ClientIdRequired()])

@target.assembly
def assemble_parser(subparsers, app):
    parser = subparsers.add_parser(
        name=target.name,
        help="manage targets stored in the WorkSpace, shows avaliable targets if no arguments are supplied.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-r', '--reset',
        help=("reset the device_code and user_code of specified target, "
            "program will block if target has non expired refresh_token."),
        dest="reset_target",
        action="store_true")
    group.add_argument('-d', '--delete',
        help=("delete target specified by {target_name}, "
            "program will block if target has non expired refresh_token."),
        dest="delete_target",
        action="store_true")
    parser.add_argument('-a', '--all',
        help=("designated all targets; can only be used with [-r] flag."),
        action='store_true',
        dest="all_targets")
    parser.add_argument('target_names',
        help=("names of the targets, creates the targets if no flags are supplied."),
        nargs="*",
        type=target_names)
    parser.add_argument('-v', '--verbose',
        help="shows the output of API.",
        action="store_true")
    parser.add_argument('--hard',
        help="overwrite the block in the [-r | -d] flags",
        dest="reset_hard",
        action="store_true")
    return parser

@target.func
def main():
    wsp_record = Wsp.select().first()
    client.client.aio = True
    if not settings.target_names:
        targets = sorted([target for target in Target.select()], key=lambda t: not t.active)
        if not settings.all_targets and not settings.reset_target:
            current_app.display(msgs.target_list(targets))
            return 
    if not settings.delete_target and not settings.reset_target:
        target_names = []
        for name in settings.target_names:
            if Target.select().where(Target.name==name).first():
                current_app.display(msgs.target_exists(name))
                continue
            target_names.append(name)
        cors = [_get_user_code(wsp_record) for _ in target_names]
        responses = client.client.loop.run_until_complete(gather(*cors))
        for json_data, name in list(zip(responses, target_names)):
            target = Target(name = name, **json_data)
            target.save()
            wsp_target = WspTarget(target = target, wsp = wsp_record)
            wsp_target.save()
            current_app.display(msgs.target_registered(target))
        return
    if settings.delete_target:
        for name in settings.target_names:
            target = Target.select().where(Target.name == name).first()
            if not target:
                current_app.display(msgs.target_not_wsp(name))
                continue
            if target.active:
                current_app.display(msgs.target_is_active(target))
                continue
            if not target.is_exp('refresh_token') and not settings.reset_hard:
                current_app.display(msgs.target_has_refresh_token(target))
                continue
            target.delete_instance()
            wsp_target = WspTarget.select().where(WspTarget.target == target.id).first()
            wsp_target.delete_instance()
            current_app.display(msgs.target_deleted(target))
    if settings.reset_target:
        if settings.target_names:
            targets = []
            for name in settings.target_names:
                target = Target.select().where(Target.name == name).first()
                if not target:
                    current_app.display(msgs.target_not_wsp(name))
                    continue
                targets.append(target)
        elif settings.all_targets:
            targets = [target for target in Target.select()]
        else:
            targets = [target for target in Target.select()\
                .join(WspTarget)\
                    .where(WspTarget.active == True)]
        targets_no_rt = []
        for target in targets:
            if not target.is_exp('refresh_token') and not settings.reset_hard:
                current_app.display(msgs.target_has_refresh_token(target))
                continue
            targets_no_rt.append(target)
        cors = [_get_user_code(wsp_record) for _ in targets_no_rt]
        responses = client.client.loop.run_until_complete(gather(*cors))
        for json_data, target in list(zip(responses, targets)):
            Target.update(**json_data, 
                refresh_token_ts = None, 
                access_token_ts = None).where(Target.id == target.id).execute()
            target = Target.select().where(Target.id == target.id).first()
            current_app.display(msgs.target_reset(target))

async def _get_user_code(wsp_record):
    r = await client.get_device_code(client_id=wsp_record.client_id, raise_on_status_code = False)
    if settings.verbose:
        current_app.display(r.json)
    if r.status != 200:
        raise CliAppError(msgs.could_not_get_user_code())
    return {
        'device_code': r.json['device_code'], 
        'user_code': r.json['user_code'],
        'device_code_ts': datetime.now(),
        'user_code_ts': datetime.now(),
        'access_token': None,
        'refresh_token': None
    }

    
    


    
