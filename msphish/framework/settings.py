class BaseSettings(object):

    def __init__(self) -> None:
        self.workspace = None

    def register_from_namespace(self, namespace):
        self.__dict__.update(**vars(namespace))

    def register_workspace(self, workspace):
        self.workspace = workspace
        if self.workspace.exists:
            self.__dict__.update(**workspace.read_in_settings())

