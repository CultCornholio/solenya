from .framework import Client, Resource

from . import constants as const

client = Client(
    base_url='https://graph.microsoft.com',
    base_headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
)

@client.endpoint
def get_emails(access_token, target_id):
    return Resource(
        uri='/v1.0/me/MailFolders/inbox/messages',
        headers={'Authorization': f'Bearer {access_token}'},
        params={'select': const.EMAIL_SELECT}
    )