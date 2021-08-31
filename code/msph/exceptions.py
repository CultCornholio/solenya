class CliAppError(Exception):
    
    def __init__(self, msg, *args, no_spacing=False) -> None:
        if not no_spacing:
            msg = f"\n\n{msg}\n"
        super().__init__(msg, *args)

class ValidationError(CliAppError):

    def __init__(self, msg, *args, no_spacing=False) -> None:
        super().__init__(msg, *args, no_spacing=no_spacing)