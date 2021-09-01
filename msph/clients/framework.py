from functools import wraps
from aiohttp import ClientSession
from asyncio import get_event_loop
from types import SimpleNamespace

class ClientError(Exception):
    pass

class Resource(SimpleNamespace):

    def __init__(self, uri:str=str(), params:dict=dict(), headers:dict=dict(),
        data:dict=dict(), json:dict=dict(), func_kwargs=dict()) -> None:
        self.uri = uri
        self.params = params
        self.headers = headers
        self.data = data
        self.json = json
        self.func_kwargs = func_kwargs

class Response(SimpleNamespace):
     
    def __init__(self, status, json, resource) -> None:
        self.json = json
        self.status = status
        self.resource = resource

class Client(object):

    def __init__(self, base_url, base_headers = None):
        self.base_url = base_url
        if base_headers:
            self.base_headers = base_headers
        else:
            self.base_headers = {}
        self.loop = get_event_loop()
        self.aio = False

    async def do_get_request(self, resource, raise_on_status_code):
        async with ClientSession(loop = self.loop) as session:
            data_or_json = {}
            if resource.data:
                data_or_json['data'] = resource.data
            if resource.json:
                data_or_json['json'] = resource.json
            async with session.get(
                    url = self.base_url + resource.uri,
                    headers={**self.base_headers, **resource.headers},
                    params=resource.params,
                    **data_or_json
                ) as r:
                json_ = await r.json()
                if r.status != 200 and raise_on_status_code:
                    raise ClientError(f'Server did not return 200. Status code: {r.status}.')
                return Response(r.status, json_, resource)

    async def handler(self, func, *args, raise_on_status_code, **kwargs):
        resource = func(*args, **kwargs)
        resource.func_kwargs = kwargs
        r = await self.do_get_request(resource, raise_on_status_code)
        return r

    def endpoint(self, func):
        @wraps(func)
        def wrapper(*args, raise_on_status_code = True, **kwargs):
            return self.handler(
                func, *args, 
                raise_on_status_code = raise_on_status_code, 
                **kwargs) if self.aio \
                else self.loop.run_until_complete(
                    self.handler(
                    func, *args, 
                    raise_on_status_code = raise_on_status_code,
                    **kwargs)
                )
        return wrapper

        
