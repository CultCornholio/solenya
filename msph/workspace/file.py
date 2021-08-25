import json

class File(object):

    def __init__(self, path, content=None) -> None:
        self.path = path
        if not content:
            self._content = {}
        else:
            self._content = content

    def read(self):
        if self._content:
            return self._content
        try:
            with open(self.path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return dict()

    def write(self, **kwargs):
        self._content = kwargs
        with open(self.path, 'w') as file:
            json.dump(kwargs, file, indent=4, ensure_ascii=False)

    def update(self, **kwargs):
        self.write(**{**self.read(), **kwargs})

        