class BaseError(Exception):
    pass

class ApplicationError(BaseError):
    pass

class ValidationError(BaseError):
    pass