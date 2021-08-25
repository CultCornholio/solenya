from functools import wraps
import requests

class ClientError(Exception):
    pass

class Resource(object):

    def __init__(self, uri:str=str(), params:dict=dict(), headers:dict=dict(),
        data:dict=dict(), json:dict=dict()) -> None:
        self.uri = uri
        self.params = params
        self.headers = headers
        self.data = data
        self.json = json

class Client(object):

    def __init__(self, base_url, base_headers = None):
        self.base_url = base_url
        if base_headers:
            self.base_headers = base_headers
        else:
            self.base_headers = {}

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
        
