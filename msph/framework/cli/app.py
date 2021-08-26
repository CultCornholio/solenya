from .settings import BaseSettings
from .cli import Router, Command

class CliApp(object):
    
    def __init__(self, name) -> None:
        self.name = name
        self.root_router = None
        self.plugins = dict()
        self.depth_string = str()
        self.register_settings(BaseSettings())

    def register_settings(self, settings):
        self.settings = settings
        self.settings.register_app(self)

    def register_plugin(self, plugin):
        plugin.register_app(self)
        self.plugins[plugin.name] = plugin

    def register_root_router(self, router):
        self.root_router = router
        self.root_router.name = self.name

    def dispatch(self, argv):
        self.prepare_dispatch()
        self._dispatch(self.root_router, argv)

    def prepare_dispatch(self):
        for plugin in self.plugins.values():
            plugin.before_propagation()

    def _dispatch(self, node, argv):
        node.validate_required(self)
        self.depth_string += f".{node.name}"
        node.create_parser(self.depth_string)
        if isinstance(node, Router):
            self._dispatch(*node.get_route(argv))
        if isinstance(node, Command):
            self._execute_command(node, argv)

    def _execute_command(self, cmd, argv):
        if cmd.registered_cli_func:
                cmd = cmd.cli_func()
                namespace = cmd.parser.parse_args(argv)
                self.settings.register_from_namespace(namespace)
        if cmd.registered_target_func:
            cmd.target_func(self.settings)
            
    
        
