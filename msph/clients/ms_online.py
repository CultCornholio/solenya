from .framework import Client, Resource

from . import constants as const

client = Client(
    base_url='https://login.microsoftonline.com',
    base_headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', 
        'Content-Type': 'application/x-www-form-urlencoded',
    }
)

@client.endpoint
def get_device_code(client_id:str) -> str:
    return Resource(
        uri='/organizations/oauth2/v2.0/devicecode',
        data={"client_id": client_id, "scope": const.DEVICE_CODE_SCOPE},
    )

@client.endpoint
def get_access_token(client_id:str, device_code:str) -> dict:
    return Resource(
        uri='/organizations/oauth2/v2.0/token',
        data={"grant_type": const.ACCESS_TOKEN_GRANT, "client_id": client_id, "code": device_code},
    )

@client.endpoint
def refresh_access_token(refresh_token:str, target_id:str) -> dict:
    return Resource(
        uri='/common/oauth2/v2.0/token',
        data={'grant_type': 'refresh_token', 'refresh_token': refresh_token, 'scope': const.DEVICE_CODE_SCOPE}
    )
