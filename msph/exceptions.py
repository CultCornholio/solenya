import colorful as cf

class CliAppError(Exception):
    
    def __init__(self, msg, *args, no_spacing=False) -> None:
        msg = f"{cf.red('ERROR')}:\n{msg}"
        super().__init__(msg, *args)

class ValidationError(CliAppError):

    def __init__(self, msg, *args, no_spacing=False) -> None:
        super().__init__(msg, *args, no_spacing=no_spacing)