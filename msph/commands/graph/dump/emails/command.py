from msph.framework.cli import Command, display

from .....clients import graph_api as client
from .....workspace.file import File
from ..... import workspace
from ..... import utils
from . import msgs


emails = Command(
    'emails',
    description='Retrieves and dumps emails from Graph API.'
)

@emails.cli()
def cli(cmd):
    cmd.parser.add_argument('-o', '--outfile',
        help="The path to output file.",
        required = True,
        type=str,
        dest="output_path"
    )
    cmd.parser.add_argument('-fm', '--format',
        help="Formats the output.",
        dest="format_output",
        action='store_true')
    return cmd

@emails.target()
def target(settings):
    r = client.get_emails(workspace.settings_file.read()['access_token'])
    json_ = r.json()
    File(settings.output_path, auto_fmt=settings.format_output).write(**json_)
    display(msgs.emails_dumped(settings.output_path))
