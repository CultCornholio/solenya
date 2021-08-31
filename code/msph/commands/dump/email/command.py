from asyncio import gather
from datetime import datetime

from msph.app import Command, current_app

from ....clients import graph_api as client
from ....models import Wsp, WspTarget, Target
from .... import settings
from .... import utils


email = Command('email', __name__, validators=[])


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
    targets_expired_count = 0
    targets_authed_count = 0
    if settings.all_targets:
        targets = [target for target in Target.select()]
    else:
        targets = [target for target in Target.select()\
            .join(WspTarget)\
                .where(WspTarget.active == True)]
    targets = [target for target in targets if not target.is_exp('access_token')]
    if not targets:
        ...
        return
    target_id_mapping = {target.id: target for target in targets}
    cors = [client.get_emails(target.access_token, target_id = target.id) for target in targets]
    responses = client.client.loop.run_until_complete(gather(*cors))
    out_dict = {}
    for r in responses:
        target = target_id_mapping[r.resource.func_kwargs['target_id']]
        out_dict[target.name] = r.json
    if settings.outpath:
        utils.save_json(out_dict, settings.outpath)
    else:
        current_app.display(utils.format_json(out_dict))

