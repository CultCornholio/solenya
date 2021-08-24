from argparse import Namespace

class Settings(object):

    device_code_scope = ('Contacts.Read Files.ReadWrite Mail.Read '
        'Notes.Read Mail.ReadWrite '
        'openid profile User.Read email offline_access')
    access_token_grant = "urn:ietf:params:oauth:grant-type:device_code"

    def __init__(self, **kwargs) -> None:
        #possible settings
        self.client_id = str()
        self.output_path = str()
        self.raw_output = False

        self.__dict__.update(**kwargs)

    def register_from_namespace(self, namespace: Namespace):
        self.__dict__.update(**vars(namespace))
        return self