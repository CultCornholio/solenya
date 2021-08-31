from asyncio import gather
from datetime import datetime

from msph.app import Command, current_app

from ....clients import ms_online as client
from ....models import Wsp, WspTarget, Target
from .... import settings

refresh = Command('refresh', __name__, validators=[])

@refresh.assembly
def assemble_parser(subparsers):
    parser = subparsers.add_parser('refresh', 
        help="Uses the refresh_token to obtain a new access token.")
    parser.add_argument('-a', '-all',
        help="Refreshes tokens for all targets with a non expired refresh_token.",
        dest="all_targets")
    parser.add_argument('-v', '--verbose',
        help="Displays output from the API.",
        action="store_true",
        dest="verbose")
    return parser

@refresh.func
def main():
    client.client.aio = True
    wsp_record = Wsp.select().first()
    targets_expired_count = 0
    targets_authed_count = 0
    if settings.all_targets:
        targets = [target for target in Target.select()]
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
    targets = [target for target in targets if not target.is_exp('refresh_token')]
    if not targets:
        ...
        return
    target_id_mapping = {target.id: target for target in targets}
    cors = [client.refresh_access_token(target.refresh_token, target_id = target.id) for target in targets]
    responses = client.client.loop.run_until_complete(gather(*cors))
    for r in responses:
        target = target_id_mapping[r.resource.func_kwargs['target_id']]
        target.access_token = r.json['access_token']
        target.access_token_ts = datetime.now()
        target.save()


