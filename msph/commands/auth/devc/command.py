from msph.framework.cli import Command, display

from ....validators import ClientIdRequired, WorkSpaceRequired
from ....clients import ms_online as client
from .... import workspace
from . import msgs

devc = Command(
    'devc', 
    description='Dumps user_id and device_code to the WorkSpace.',
    required=[ClientIdRequired()]
)

@devc.cli()
def cli(cmd):
    cmd.parser.add_argument('-v', '--verbose', 
        help="Verbose output of API status calls to check for Oauth token.",
        action='store_true')
    return cmd

@devc.target()
def target(settings):
    r = client.get_device_code(settings.client_id)
    if settings.verbose:
        display(r.json())
    codes = {
        'user_code': r.json()['user_code'],
        'device_code': r.json()['device_code']
    }
    workspace.settings_file.update(**codes)
    display(msgs.create_instructions_msg())
    display(msgs.create_devc_message(**codes))
    

    

