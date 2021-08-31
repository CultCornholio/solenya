from asyncio import gather
from datetime import date, datetime
import os

from msph.app import Command, current_app

from ....exceptions import CliAppError
from ....clients import graph_api as client
from ....models import Wsp, WspTarget, Target
from .... import settings, wsp
from .... import utils
from ....validators import ActiveTargetRequired


email = Command('email', __name__, validators=[ActiveTargetRequired()])


@email.assembly
def assemble_parser(subparsers):
    parser = subparsers.add_parser(email.name,
        help="Fetches all e-mails from the inbox using the Microsoft Graph API and saves them to a file")
    parser.add_argument('-a', '--all',
        help="Collects all e-mails for every target in the workspace",
        action="store_true",
        dest="all_targets")
    parser.add_argument('-v', '--verbose',
        help="Displays output from the API.",
        action="store_true",
        dest="verbose")
    parser.add_argument('-o', '--output',
        help="Specify the path where emails should be saved",
        dest="outpath")
    return parser

@email.func
def main():
    client.client.aio = True
    wsp_record = Wsp.select().first()
    if settings.all_targets:
        targets = [target for target in Target.select()]
        print('Running dump for all targets...')
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
        print('Running dump for active target...')
    updated_targets = []
    for target in targets:
        if target.is_exp('access_token'):
            print('WARNING: target name has an expired access token. Skipping...')
            continue
        updated_targets.append(target)
    targets = updated_targets
    if not targets:
        raise CliAppError('Target/Targets do not have valid access tokens')
    target_id_mapping = {target.id: target for target in targets}
    cors = [client.get_emails(target.access_token, target_id = target.id, raise_on_status_code = False) for target in targets]
    responses = client.client.loop.run_until_complete(gather(*cors))
    out_dict = {}
    for r in responses:
        target = target_id_mapping[r.resource.func_kwargs['target_id']]
        if r.code != 200:
            print('Could not get emails. Status code: {}')
            continue
    out_dict[target.name] = r.json

    if settings.outpath:
        file_path = settings.outpath
    else:
        file_path = os.path.join(wsp.root_dir, f"emails.{datetime.now().isoformat(sep='T')}.json")
    utils.save_json(out_dict, file_path)
    print('file saved to file...')

