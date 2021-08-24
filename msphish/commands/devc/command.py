from msphish.framework.cli import Command
from msphish.framework.types.exceptions import ApplicationError

from . import msgs

init = Command(
    'devc', 
    description='Dumps the device code.',
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
def target(app):
    if app.workspace.exists:
        if not app.settings.hard:
            raise ApplicationError(msgs.create_workspace_exists_msg())
        app.workspace.clear()
    app.workspace.create()
    app.workspace.register_client_id(
        app.settings.client_id)
    app.display(msgs.create_client_id_registered_msg(app.settings.client_id))