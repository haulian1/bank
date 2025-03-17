import uuid
from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4

from models.Enums import BankTransactionStatus, BankTransactionType
from models.errors_and_exceptions.InvalidInitializationError import InvalidInitializationError
from models.errors_and_exceptions.UnknownTransactionTypeError import UnknownTransactionTypeError


@dataclass
class BankTransaction:
    origin_account: uuid
    destination_account: uuid
    amount: float
    status: BankTransactionStatus
    transaction_id: uuid = uuid4()
    errors: list[(datetime, Exception)] = field(default_factory=list[(datetime, Exception)])

    def __post_init__(self):
        now = datetime.now()
        if self.origin_account is None and self.destination_account is None:
            self.errors.append(
                (
                    now,
                    InvalidInitializationError(f'Bank transaction must have an origin or destination account')
                )
            )
        elif self.origin_account == self.destination_account:
            self.errors.append(
                (
                    now,
                    InvalidInitializationError(f'Bank transactions cannot have the same origin and destination account')
                )
            )

    def __eq__(self, other):
        if isinstance(other, BankTransaction):
            return self.transaction_id == other.transaction_id
        return False

    def __str__(self):
        return (f'Origin: {self.origin_account if self.origin_account else 'NONE'}\n'
                f'Destination: {self.destination_account if self.destination_account else 'NONE'}\n'
                f'Amount: {self.amount}\n'
                f'Status: {self.status}\n'
                f'Transaction ID: {self.transaction_id}')

    def __hash__(self):
        return self.transaction_id.__hash__()


def determine_bank_transaction_type(destination_id: uuid, transaction: BankTransaction) -> BankTransactionType:
    match destination_id:
        case transaction.destination_account:
            return BankTransactionType.Deposit
        case transaction.origin_account:
            return BankTransactionType.Withdrawal
        case _:
            raise UnknownTransactionTypeError(destination_id, transaction)
