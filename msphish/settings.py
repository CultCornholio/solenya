from .framework.settings import BaseSettings

class Settings(BaseSettings):

    workspace_root_folder = './msph/'
    device_code_scope = ('Contacts.Read Files.ReadWrite Mail.Read '
        'Notes.Read Mail.ReadWrite '
        'openid profile User.Read email offline_access')
    access_token_grant = "urn:ietf:params:oauth:grant-type:device_code"

    def __init__(self) -> None:
        #possible settings
        self.client_id = str()
        self.output_path = str()
        self.raw_output = False

