class BaseError(Exception):
    pass

class ClientError(BaseError):
    pass

class ApplicationError(BaseError):
    pass