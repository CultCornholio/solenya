from msph.frameworks.cli import Command

email = Command('users', description='Dumps the users from Graph API.')

@email.cli()
def cli(cmd):
    cmd.parser.add_argument('client_id',
        help="The id of the application.",
        type=str)
    return cmd

@email.target()
def target(app):
    app.workspace