import uuid
from dataclasses import dataclass
from datetime import datetime

from Enums import BankTransactionType, Status
from Exceptions import InvalidTransactionException


@dataclass
class Transaction:
    transaction_type: BankTransactionType
    amount: float
    source: uuid
    destination: uuid
    status: Status
    date_initiated: datetime
    date_updated: datetime
    date_finalized: datetime

    def __post_init__(self):
        cur_time = datetime.now()
        if self.transaction_type is None:
            if self.source is None and self.destination is None:
                raise InvalidTransactionException('No source or destination')
            elif self.source is None:
                self.transaction_type = BankTransactionType.DEPOSIT
            elif self.destination is None:
                self.transaction_type = BankTransactionType.WITHDRAWAL
            else:
                self.transaction_type = BankTransactionType.TRANSFER

        if self.date_initiated is None:
            self.date_initiated = cur_time
            self.date_updated = cur_time

        if (self.status in [Status.FAILED, Status.SUCCESS]
                and self.date_finalized is None):
            self.date_finalized = cur_time

    def __str__(self):
        return (f'{self.transaction_type.name}'
                f'\n$ {self.amount}'
                f'{'' if self.source is None else f'\nFrom: {self.source}'}'
                f'{'' if self.destination is None else f'\nTo: {self.destination}'}'
                f'\n{self.status.name}')
