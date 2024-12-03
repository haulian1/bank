from enum import Enum


class CardinalDirections(Enum):
    NONE = -1
    E = 0
    NE = 1
    N = 2
    NW = 3
    W = 4
    SW = 5
    S = 6
    SE = 7


class BankAccountType(Enum):
    CHECKING = 1
    SAVINGS = 2


class BankTransactionType(Enum):
    OPEN_ACCOUNT = 1
    DEPOSIT = 2
    WITHDRAWAL = 3
    TRANSFER = 4


class Status(Enum):
    NOT_STARTED = -1
    SUCCESS = 0
    FAILED = 1
    IN_PROGRESS = 2
