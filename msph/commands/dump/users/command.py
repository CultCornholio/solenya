from msph.frameworks.cli import Command

init = Command('users', description='Dumps the users from Graph API.')

@init.cli()
def cli(cmd):
    cmd.parser.add_argument('client_id',
        help="The id of the application.",
        type=str)
    return cmd

@init.target()
def target(app):
    app.workspace