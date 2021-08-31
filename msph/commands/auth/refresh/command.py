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
    if settings.all_targets:
        targets = [target for target in Target.select()]
        print('Running refresh for all targets with valid refresh_token: count...')
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
        print('Running refresh for active target: info...')
    updated_targets = []
    for target in targets:
        if target.is_exp('refresh_token'):
            print('WARNING: target does not have a valid refresh token... Skiping...')
            continue
    targets = updated_targets
    target_id_mapping = {target.id: target for target in targets}
    cors = [client.refresh_access_token(
        target.refresh_token, target_id = target.id, raise_on_status_code = False) for target in targets]
    responses = client.client.loop.run_until_complete(gather(*cors))
    for r in responses:
        target = target_id_mapping[r.resource.func_kwargs['target_id']]
        if r.status != 200:
            print('Could not get access token... Skipping...')
            continue
        target.access_token = r.json['access_token']
        target.access_token_ts = datetime.now()
        target.save()
        print('SUCCESS: access token updated for target....')


