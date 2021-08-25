import json

class File(object):

    def __init__(self, path) -> None:
        self.path = path
    def read(self):
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return dict()

    def write(self, **kwargs):
        with open(self.path, 'w') as file:
            json.dump(kwargs, file, indent=4, ensure_ascii=False)

    def update(self, **kwargs):
        self.write(**{**self.read(), **kwargs})

        