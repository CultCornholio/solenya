from types import SimpleNamespace
from functools import wraps
import inspect
import sys

from .exceptions import CliAppError
from .settings import Settings

current_app = None

class CliApp(object):

    def __init__(self, name) -> None:
        self.name = name
        self.plugins = SimpleNamespace()
        self.settings = None
        self.parser = None
        self.active_command = None
        self.commands = {}
        global current_app; current_app=self

    def display(self, msg, padding=False):
        if padding:
            msg = f"\n{msg}\n"
        print(msg)

    def register_settings(self, settings):
        settings.register_app(self)
        self.settings = settings

    def register_command(self, command):
        path = '.'.join(list(filter(
            lambda val: 'command' not in val, 
            command._name_.split('.')
        )))
        self.commands[path] = command

    def register_plugin(self, plugin):
        setattr(self.plugins, plugin.name, plugin)
        plugin.register_app(self)

    def register_parser(self, parser):
        self.parser = parser

    def cli_validator(self, func):
        self._custom_validators.append(func)

    def register_config(self, config):
        self.config = {k:v for k, v in config.__dict__.items() if k.isupper()}
    
    def run_command(self, command_path, settings):
        active_command_bak = self.active_command
        settings_bak = Settings().register_from_namespace(self.settings)
        try:
            self.current_command = self.commands[command_path]
        except KeyError:
            raise CliAppError(f'Command {command_path} is not registered with the application')
        else:
            self.settings.clear().register_from_namespace(settings)
            self.current_command.default_func()
            self.current_command = active_command_bak
            self.settings.clear().register_from_namespace(settings_bak)
        
    def dispatch(self, argv):
        if not self.parser:
            raise CliAppError('Parser is not registered.')
        if not argv:
            self.parser.print_help()
            sys.exit()
        args = self.parser.parse_args(argv)
        self.settings.register_from_namespace(args)
        args.func()

class Command(object):
    
    def __init__(self, name, _name_, validators = None) -> None:
        self.name = name
        self._name_ = _name_
        self.app = None
        self.assemble_parser = None
        self.default_func = None
        self.parser = None
        if not validators:
            validators = []
        self.validators = validators

    def assembly(self, func):
        self.assemble_parser = self._register_parser(func)

    def _register_parser(self, func):
        def wrapper(*args, app, **kwargs):
            self.app = app
            app.register_command(self)
            app_kw = {'app': self.app} if 'app' in inspect.getargspec(func).args else {}
            self.parser = func(*args, **app_kw, **kwargs)
            if self.default_func:
                self.parser.set_defaults(func=self.default_func)
            return self.parser
        return wrapper

    def func(self, func):
        self.default_func = self._func_wrapper(func)
            
    def _func_wrapper(self, func):
        def wrapper(*args, **kwargs):
            self.app.active_command = self
            for validator in self.validators:
                validator.validate()
            return func(*args, **kwargs)
        return wrapper

class Validator(object):

    def validate(self):
        pass



LICENSE = """
MIT License

Copyright (c) 2021 Artur Saradzhyan, Alex Martirosyan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""