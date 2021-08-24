from ..clients.base import Client
from ..types.resource import Resource
from ..settings import Settings


client = Client('https://login.microsoftonline.com')

@client.endpoint
def get_device_code(client_id:str) -> str:
    return Resource(
        uri='/organizations/oauth2/v2.0/devicecode',
        data={"client_id": client_id, "scope": Settings.device_code_scope},
    )

@client.endpoint
def get_access_token(client_id:str, device_code:str) -> dict:
    return Resource(
        uri='/organizations/oauth2/v2.0/token',
        data={"grant_type": Settings.grant, "client_id": client_id, "code": device_code},
    )


