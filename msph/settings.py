from types import SimpleNamespace
import os

class Settings(SimpleNamespace):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.app = None
        
        #possible settings
        self.target_name = None
        self.delete_target = False
        self.reset_target = False
        self.reset_hard = False
        self.client_id = None
        self.verbose = False
        self.wsp_reset = False
        self.create_target = False
        self.monitor = False
        self.all_targets = False
        self.target_names = []
        self.outpath = ''

        self.__dict__.update(**kwargs)

    def register_app(self, app):
        self.app = app

    def clear(self):
        self.register_from_namespace(Settings(app=self.app))
        return self
        
    def register_from_namespace(self, namespace):
        self.__dict__.update(**vars(namespace))
        return self

    def register_from_dict(self, dict_):
        self.__dict__.update(**dict_)
        return self
    
