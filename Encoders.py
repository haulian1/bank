import uuid
from datetime import date

from Models.Address import Address
from Enums import CardinalDirections, BankTransactionType, Status
from Exceptions import EncodingNotFoundException


def address_encoder(obj):
    if isinstance(obj, CardinalDirections):
        return obj.name
    raise EncodingNotFoundException(obj, type(obj))

def person_encoder(obj):
    if isinstance(obj, date):
        return f'{date.year}/{date.month}/{date.day}'
    if isinstance(obj, Address):
        return str(obj)
    if isinstance(obj, uuid.UUID):
        return str(obj)
    raise EncodingNotFoundException(obj, type(obj))

def transaction_encoder(obj):
    if isinstance(obj, BankTransactionType):
        return obj.name
    if isinstance(obj, uuid.UUID):
        return str(obj)
    if isinstance(obj, Status):
        return obj.name