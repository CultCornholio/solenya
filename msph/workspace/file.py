import json

class File(object):

    def __init__(self, path, auto_fmt=True, content=None) -> None:
        self.path = path
        self.fmt = {}
        if auto_fmt:
            self.fmt = dict(indent=4, ensure_ascii=False)
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
            json.dump(kwargs, file, **self.fmt)

    def update(self, **kwargs):
        self.write(**{**self.read(), **kwargs})

        