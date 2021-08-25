from msph.frameworks.client import Client, Resource

from . import constants as const

client = Client('https://login.microsoftonline.com')

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


