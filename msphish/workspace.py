import os
import json
import shutil

class WorkSpace(object):

    def __init__(self) -> None:
        self.settings = None

    def read_in_json(self, path):
        with open(path, 'r') as file:
            return json.load(file)

    def create_json(self, path, obj):
        with open(path, 'w') as file:
            return json.dump(obj, file, indent=4, ensure_ascii=False) 

    def update_json(self, path, obj):
        existing = self.read_in_json(path)
        obj = {**obj, **existing}
        self.create_json(path, obj)

    def read_in_settings(self):
        return self.read_in_json(os.path.join(
            self.settings.workspace_root_folder,
            'settings.json'
        ))
            
    def register_settings(self, settings):
        self.settings = settings

    @property
    def exists(self):
        return os.path.isdir(self.settings.workspace_root_folder)

    def clear(self):
        shutil.rmtree(self.settings.workspace_root_folder)
    
    def create(self):
        os.mkdir(self.settings.workspace_root_folder)
        self.create_json(
            path = os.path.join(self.settings.workspace_root_folder,
                'settings.json'),
            obj = {})

    def register_client_id(self, client_id):
        self.update_json(
            path = os.path.join(self.settings.workspace_root_folder,
                'settings.json'),
            obj = {'client_id': client_id})

    
