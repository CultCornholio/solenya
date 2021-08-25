import os
import shutil

from msph.framework.cli.plugin import Plugin
from msph.framework.cli.exceptions import ApplicationError

from .file import File

class WorkSpace(Plugin):

    def __init__(self, hidden) -> None:
        self.name = 'workspace'
        self.hidden = hidden
        Plugin.__init__(self)

    def before_propagation(self):
        prefix = '.' if self.hidden else ''
        self.root_dir = f"{prefix}{self.app.name}"
        self.settings_file = File(os.path.join(self.root_dir, 'assets.json'))
        self.app.settings.register_from_dict(self.settings_file.read())

    def clear(self):
        shutil.rmtree(self.root_dir)
    
    def create(self):
        os.mkdir(self.root_dir)
        self.settings_file.write()

    @property
    def exists(self):
        return os.path.isdir(self.root_dir)

    



