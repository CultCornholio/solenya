from .plugin import Plugin

class BaseSettings(Plugin):

    def __init__(self) -> None:
        Plugin.__init__(self)

    def register_from_namespace(self, namespace):
        self.__dict__.update(**vars(namespace))

    def register_from_dict(self, dict_):
        self.__dict__.update(**dict_)