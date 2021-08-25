from msph.framework.cli import Command, display

from ....validators import RefreshTokenRequired
from ....clients import ms_online as client
from . import msgs
from .... import workspace

refresh = Command(
    'refresh',
    description='Refreshes the access token using refresh token.',
    required=[RefreshTokenRequired()]
)

@refresh.cli()
def cli(cmd):
    cmd.parser.add_argument('-v', '--verbose', 
        help="Verbose output of API status calls to check for Oauth token.",
        action='store_true')
    return cmd

@refresh.target()
def target(settings):
    r = client.refresh_access_token(workspace.settings_file.read()['refresh_token'])
    if settings.verbose:
        display(r.json())
    workspace.settings_file.update(access_token = r.json()['access_token'])
    display(msgs.create_token_refreshed_msg())