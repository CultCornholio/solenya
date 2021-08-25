import time

from msph.framework.cli import Command, display, ApplicationError

from ....validators import ClientIdRequired, DeviceCodeRequired
from ....clients import ms_online as client
from .... import workspace
from . import msgs

phish = Command(
    'phish', 
    description='Fetches the OAuth tokens in the following format access code, refresh token, and id token',
    required=[ClientIdRequired(), DeviceCodeRequired()]
)

@phish.cli()
def cli(cmd):
    cmd.parser.add_argument('-v', '--verbose', 
        help="Verbose output of API status calls to check for Oauth token",
        action='store_true')
    cmd.parser.add_argument('-m', '--monitor',
        help="Fetch the OAuth tokens incrementally making API calls in monitor mode, this is preferred",
        action='store_true'
    )
    return cmd

@phish.target()
def target(settings):
    while True:
        r = client.get_access_token(settings.client_id, settings.device_code,
            raise_on_status_code=False)
        if settings.verbose:
            display(r.json())
        if r.json().get('error') == 'authorization_pending':
            display(msgs.create_auth_pending())
            if not settings.monitor:
                raise ApplicationError(msgs.create_auth_pending())
        if r.json().get('error') == 'expired_token':
            raise ApplicationError(msgs.create_auth_expired())
        if r.status_code == 200:
            tokens = {
                'access_token': r.json()['access_token'],
                'refresh_token': r.json()['refresh_token'],
                'id_token': r.json()['id_token']
            }
            break
        time.sleep(1)
    workspace.settings_file.update(**tokens)
    display(msgs.create_auth_success())


