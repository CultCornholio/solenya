from msph.frameworks.cli import Command

from . import msgs
from ... import workspace
from ...validators import ClientIdRequired, WorkSpaceRequired

devc = Command(
    'devc', 
    description='Dumps the device code and user code.',
    required=[ClientIdRequired(), WorkSpaceRequired()]
)

@devc.cli()
def cli(cmd):
    cmd.parser.add_argument('-o', '--outfile',
        help="Destination to save the user_id and device_code to. Saved in msph/settings.json otherwise.",
        type=str)
    return cmd

@devc.target()
def target(app):
    ...