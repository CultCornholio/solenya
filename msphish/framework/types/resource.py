class Resource(object):

    def __init__(self, uri:str=str(), params:dict=dict(), headers:dict=dict(),
        data:dict=dict(), json:dict=dict()) -> None:
        self.uri = uri
        self.params = params
        self.headers = headers
        self.data = data
        self.json = json
        
    