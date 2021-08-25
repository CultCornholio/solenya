from msph.framework.cli import Command, display
from msph.framework.cli.exceptions import ApplicationError

from . import msgs
from .... import workspace

init = Command(
    'init', 
    description='Initializes the workspace.',
)

@init.cli()
def cli(cmd):
    cmd.parser.add_argument('client_id',
        help="The id of the application.",
        type=str)
    cmd.parser.add_argument('--hard',
        help="Overwrite existing workspace.",
        action="store_true")
    return cmd

@init.target()
def target(settings):
    if workspace.exists:
        if not settings.hard:
            raise ApplicationError(msgs.create_workspace_exists_msg())
        workspace.clear()
    workspace.create()
    workspace.settings_file.update(client_id = settings.client_id)
    display(msgs.create_client_id_registered_msg(settings.client_id))