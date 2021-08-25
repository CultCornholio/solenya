from msph.frameworks.cli import BaseSettings

class Settings(BaseSettings):

    def __init__(self) -> None:
        BaseSettings.__init__(self)

        #possible settings
        self.client_id = str()
        self.hard = False
        self.out_file = str()