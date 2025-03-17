from enum import Enum


class BankAccountStatus(Enum):
    Active = 1
    Inactive = 0
    Closed = -1

class BankTransactionType(Enum):
    Deposit = 1
    OpenAccount = 0
    Withdrawal = -1
    CloseAccount = -2

class BankTransactionStatus(Enum):
    Error = -2
    Canceled = -1
    Initiated = 0
    InProgress = 1
    Success = 2
