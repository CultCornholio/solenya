from functools import wraps
import requests

from .types.exceptions import ClientError

class Client(object):

    def __init__(self, base_url, base_headers = None):
        self.base_url = base_url
        if base_headers:
            self.base_headers = base_headers
        else:
            self.base_headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0', 
            'Content-Type': 'application/x-www-form-urlencoded',
        }

    def endpoint(self, func):
        @wraps(func)
        def wrapper(*args, raise_on_status_code=True, **kwargs):
            resource = func(*args, **kwargs)
            r = requests.get(self.base_url + resource.uri,
                headers={**self.base_headers, **resource.headers},
                params=resource.params,
                data=resource.data,
                json=resource.json)
            if r.status_code != 200 and raise_on_status_code:
                raise ClientError(f'server encountered an error (status code: {r.status_code})')
            return r
        return wrapper