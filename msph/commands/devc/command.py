from msph.frameworks.cli import Command, display

from ...validators import ClientIdRequired, WorkSpaceRequired
from ...clients import ms_online as client
from ... import workspace
from . import msgs
from ...workspace.types import File

devc = Command(
    'devc', 
    description='Dumps user_id and device_code to the WorkSpace',
    required=[WorkSpaceRequired(), ClientIdRequired()]
)

@devc.cli()
def cli(cmd):
    cmd.parser.add_argument('-o', '--out', 
        help="File to which the device_code and user_code will be written to.",
        dest='out_path',
        type=str)
    return cmd

@devc.target()
def target(settings):
    r = client.get_device_code(settings.client_id)
    codes = {
        'user_code': r.json()['user_code'],
        'device_code': r.json()['device_code']
    }
    workspace.settings_file.update(**codes)
    if settings.out_path:
        File(settings.out_path).write(**codes)
    display(msgs.create_instructions_msg())
    display(msgs.create_devc_message(**codes))
    

    

