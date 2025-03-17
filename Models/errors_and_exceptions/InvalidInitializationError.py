from dataclasses import dataclass


@dataclass
class InvalidInitializationError(RuntimeError):
    message: str
    error_code: int
    def __init__(self, message: str, error_code: int = -1):
        super().__init__(f'Invalid arguments during initialization.\n'
                         f'Error Code: {error_code}'
                         f'Inner exception was: `{message}`')
        self.message = message
        self.error_code = error_code