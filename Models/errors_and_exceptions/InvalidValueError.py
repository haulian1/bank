from dataclasses import dataclass


@dataclass
class InvalidValueError(Exception):
    message: str
    error_code: int

    def __init__(self, message: str, error_code):
        super().__init__(f'Invalid value was entered.\n'
                         f'Inner exception was: {message}')
        self.message = message
        self.error_code = error_code
