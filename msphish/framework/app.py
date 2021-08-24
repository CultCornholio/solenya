import argparse

from .types.exceptions import ApplicationError
from .cli import Router, Command

class App(object):
    
    def __init__(self, name) -> None:
        self.name = name
        self.root_router = None
        self.descendants = {}
        self.settings = None
        self.workspace = None

    def register_settings(self, settings):
        self.settings = settings()

    def register_workspace(self, workspace):
        self.workspace = workspace()

    def register_root_router(self, router):
        self.root_router = router

    def display(self, msg):
        print(msg)

    def propagate(self, argv):
        self.prepare_propagation()
        self._propagate(argv, self.root_router)

    def prepare_propagation(self):
        if not self.root_router:
            raise ApplicationError('Root router not registered.')
        if not self.settings:
            raise ApplicationError('Settings not registered.')
        if not self.workspace:
            raise ApplicationError('Workspace not registered')
        self.workspace.register_settings(self.settings)
        self.settings.register_workspace(self.workspace)

    def _propagate(self, argv, node):
        if isinstance(node, Router):
            route, remainder = node.get_route(argv)
            self._propagate(remainder, route)
        if isinstance(node, Command):
            if node.registered_cli_func:
                cmd = node.cli_func()
                namespace = cmd.parser.parse_args(argv)
                self.settings.register_from_namespace(namespace)
            if node.registered_target_func:
                node.target_func(self)
            
    
        
