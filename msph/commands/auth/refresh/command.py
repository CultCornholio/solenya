from asyncio import gather
from datetime import datetime

from msph.app import Command, current_app

from ....clients import ms_online as client
from ....models import WspTarget, Target
from .... import settings
from . import msgs

refresh = Command('refresh', __name__, validators=[])

@refresh.assembly
def assemble_parser(subparsers):
    parser = subparsers.add_parser('refresh', 
        help="obtain a fresh access token using the refresh token.")
    parser.add_argument('-a', '--all',
        help="refresh tokens for all targets with a non expired refresh_token.",
        action="store_true",
        dest="all_targets")
    parser.add_argument('-v', '--verbose',
        help="display output from the API.",
        action="store_true",
        dest="verbose")
    return parser

@refresh.func
def main():
    client.client.aio = True
    if settings.all_targets:
        targets = [target for target in Target.select()]
        current_app.display(msgs.checking_for_all_targets(targets))
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
        current_app.display(msgs.checking_for_active_target(targets[0]))
    updated_targets = []
    for target in targets:
        if target.is_exp('refresh_token'):
            current_app.display(msgs.no_refresh_token(target))
            continue
        updated_targets.append(target)
    targets = updated_targets
    target_id_mapping = {target.id: target for target in targets}
    cors = [client.refresh_access_token(
        target.refresh_token, target_id = target.id, raise_on_status_code = False) for target in targets]
    responses = client.client.loop.run_until_complete(gather(*cors))
    for r in responses:
        target = target_id_mapping[r.resource.func_kwargs['target_id']]
        if r.status != 200:
            current_app.display(msgs.could_not_get_access_token(target))
            continue
        target.access_token = r.json['access_token']
        target.access_token_ts = datetime.now()
        target.save()
        current_app.display(msgs.access_token_success(target))
        


