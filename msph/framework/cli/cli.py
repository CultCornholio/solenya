import argparse

class Node(object):

    def __init__(self, name, description, required = None) -> None:
        self.app = None
        self.name = name
        self.description = description
        if not required:
            self.required = list()
        else:
            self.required = required

    def create_parser(self, depth_string):
        name = ' '.join(depth_string.split('.'))
        self.parser = argparse.ArgumentParser(
            prog=name, 
            description=self.description)

    def validate_required(self, app):
        for req in self.required:
            req.validate(app)
            
class Command(Node):

    def __init__(self, name, description, required = None) -> None:
        Node.__init__(self, name, description, required)
        self.registered_cli_func = None
        self.registered_target_func = None

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
            
class Router(Node):

    def __init__(self, name, description, required = None) -> None:
        Node.__init__(self, name, description, required)
        self.registered_routes = {}

    def register_route(self, route):
        self.registered_routes[route.name] = route

    def get_route(self, argv):
        self.parser.add_argument('command',
            choices = self.registered_routes.keys(),
            help = f'The action {self.name} should execute.')
        self.parser.add_argument(
            "args", help = argparse.SUPPRESS, nargs = argparse.REMAINDER,)
        args = self.parser.parse_args(argv)
        return self.registered_routes[args.command], args.args

def display(msg):
    print(msg)
