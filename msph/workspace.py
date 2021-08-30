from peewee import SqliteDatabase
import os
import shutil

class WorkSpace(object):

    name = 'wsp'

    def __init__(self) -> None:
        self.db = None
        self.app = None

    def register_app(self, app):
        self.app = app
        self.root_dir = self.app.config.get('WSP_ROOT_DIR')
        if not self.root_dir:
            self.root_dir = './'
        self.db = SqliteDatabase(os.path.join(self.root_dir, 'app.db'))

    def create(self):
        os.mkdir(self.root_dir)

    def connect_db(self):
        self.db.connect()
    
    def create_tables(self, *args):
        self.db.create_tables(args)

    @property
    def exists(self):
        return os.path.isdir(self.root_dir)

    def clear(self):
        shutil.rmtree(self.root_dir)