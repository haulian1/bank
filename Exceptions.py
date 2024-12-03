class EncodingNotFoundException(Exception):
    def __init__(self, obj, obj_type):
        super().__init__(f'Cannot encode object: {obj} of type: {obj_type}.')

class InvalidTransactionException(Exception):
    def __init__(self, message: str):
        super().__init__(message)