class Plugin(object):

    def __init__(self) -> None:
        self.app = None

    def register_app(self, app):
        self.app = app

    def before_propagation(self):
        pass
    
    def after_propagation(self):
        pass