from .settings import BaseSettings
from .exceptions import ApplicationError
from .cli import Router, Command

class App(object):
    
    def __init__(self, name) -> None:
        self.name = name
        self.root_router = None
        self.plugins = dict()
        self.depth_string = str()

        self.overwrite_settings(BaseSettings())

    def overwrite_settings(self, settings):
        self.settings = settings
        self.settings.register_app(self)

    def register_plugin(self, plugin):
        plugin.register_app(self)
        self.plugins[plugin.name] = plugin

    def register_root_router(self, router):
        self.root_router = router
        self.root_router.name = self.name

    def propagate(self, argv):
        self.prepare_propagation()
        self._propagate(argv, self.root_router)

    def prepare_propagation(self):
        for plugin in self.plugins.values():
            plugin.before_propagation()

    def _propagate(self, argv, node):
        node.validate_required(self)
        self.depth_string += node.name
        node.create_parser(self.depth_string)
        if isinstance(node, Router):
            route, remainder = node.get_route(argv)
            self._propagate(remainder, route)
        if isinstance(node, Command):
            if node.registered_cli_func:
                cmd = node.cli_func()
                namespace = cmd.parser.parse_args(argv)
                self.settings.register_from_namespace(namespace)
            if node.registered_target_func:
                node.target_func(self.settings)
            
    
        
