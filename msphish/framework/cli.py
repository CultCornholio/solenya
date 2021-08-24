import argparse

class Command(object):

    def __init__(self, name, description, dest=None) -> None:
        self.name = name
        self.description = description
        self.dest = dest if dest else name
        self.registered_cli_func = None
        self.registered_target_func = None
        self.parser = argparse.ArgumentParser(
            prog=self.name, 
            description=self.description)

    def cli(self):
        def layer(func):
            self.registered_cli_func = func
        return layer

    def target(self):
        def layer(func):
            self.registered_target_func = func
        return layer

    def cli_func(self):
        return self.registered_cli_func(self)

    def target_func(self, app):
        return self.registered_target_func(app)
            
class Router(object):

    def __init__(self, name, description, dest=None) -> None:
        self.name = name
        self.description = description
        self.dest = dest if dest else name
        self.registered_routes = {}

    def register_route(self, route):
        self.registered_routes[route.dest] = route

    def get_route(self, argv):
        parser = argparse.ArgumentParser(
            prog=self.name, description=self.description)
        parser.add_argument('command',
            choices = self.registered_routes.keys(),
            help = f'The action {self.name} should execute.')
        parser.add_argument(
            "args", help = argparse.SUPPRESS, nargs = argparse.REMAINDER,)
        args = parser.parse_args(argv)
        return self.registered_routes[args.command], args.args
