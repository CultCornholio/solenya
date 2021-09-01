from datetime import datetime

from msph.app import Command, current_app
from msph.clients import ms_online as client

from ... import wsp, settings
from ...exceptions import CliAppError
from .validators import client_id
from . import msgs
from ...models import Target, Wsp, WspTarget

wsp_cmd = Command('wsp', __name__,
    validators=[])

@wsp_cmd.assembly
def assemble_parser(subparsers):
    parser = subparsers.add_parser(wsp_cmd.name,
        help='initialize the WorkSpace.')
    parser.add_argument('client_id',
        help='client id of the application with needed permissions.',
        type=client_id)
    parser.add_argument('-t --target',
        help="specify active target name, 'default' otherwise.",
        default="default",
        dest="target_name")
    parser.add_argument('--reset-hard',
        help="reset existing WorkSpace.",
        dest="wsp_reset",
        action='store_true')
    parser.add_argument('-v', '--verbose',
        help="show output of API.",
        dest="verbose",
        action='store_true')
    return parser

@wsp_cmd.func
def main():
    if wsp.exists:
        if not settings.wsp_reset:
            raise CliAppError(msgs.workspace_exists(current_app))
        wsp.clear()
    wsp.create()
    wsp.connect_db()
    wsp.db.create_tables([Target, Wsp, WspTarget])
    wsp_record = Wsp(client_id = settings.client_id)
    wsp_record.save()
    try:
        r = client.get_device_code(settings.client_id, raise_on_status_code = False)
        if settings.verbose:
            current_app.display(r.json)
        if r.status != 200:
            raise Exception
    except:
        raise CliAppError(msgs.invalid_client_id(settings))
    else:
        target = Target(
            name=settings.target_name,
            **r.json,
            user_code_ts = datetime.now(),
            device_code_ts = datetime.now()
        )
        target.save()
        WspTarget(
            wsp = wsp_record,
            target = target,
            active = True
        ).save()
        current_app.display(msgs.workspace_created(settings, wsp, target))
        

    


    