import uuid
from dataclasses import dataclass, field
from datetime import datetime
from logging import exception
from uuid import uuid4

from models.BankTransaction import BankTransaction, determine_bank_transaction_type
from models.Enums import BankAccountStatus, BankTransactionType, BankTransactionStatus
from models.Person import Person
from models.errors_and_exceptions.InsufficientFundsError import InsufficientFundsError
from models.errors_and_exceptions.TransactionNotFoundError import TransactionNotFoundError


@dataclass
class BankAccount:
    owner: list[Person]
    balance: float = 0.0
    status: BankAccountStatus = BankAccountStatus.Active
    id: uuid = uuid4()
    transactions: dict[datetime, list[BankTransaction]] = field(default_factory=dict)

    def process_transaction(
            self,
            time_stamp: datetime,
            transaction: BankTransaction) -> BankTransaction:
        exception = None
        match determine_bank_transaction_type(self.id, transaction):
            case BankTransactionType.Deposit:
                transaction.status, exception = self.deposit(transaction.amount)
            case BankTransactionType.Withdrawal:
                transaction.status, exception = self.withdraw(transaction.amount)
            case BankTransactionType.OpenAccount:
                self.transactions[time_stamp] = [transaction]
                return transaction

        if exception:
            transaction.errors.append((datetime.now(), exception))
        if not self.transactions[time_stamp]:
            self.transactions[time_stamp] = []
        self.transactions[time_stamp].append(transaction)
        return transaction

    def update_transaction(
            self,
            time_stamp: datetime,
            transaction_id: uuid,
            updated_transaction: BankTransaction) -> (bool, Exception):
        transactions = self.transactions[time_stamp]
        if transactions:
            for index, transaction in enumerate(transactions):
                if transaction.transaction_id == transaction_id:
                    transactions[index] = updated_transaction
                    return True, None
        return False, TransactionNotFoundError(time_stamp, transaction_id, self.id, None)

    def change_account_status(self, new_state: BankAccountStatus) -> BankAccountStatus:
        self.status = new_state
        return self.status

    def deposit(self, amount: float) -> (BankTransactionStatus, Exception):
        self.balance += amount
        return BankTransactionStatus.Success, None

    def withdraw(self, amount: float) -> (BankTransactionStatus, Exception):
        if amount > self.balance:
            return BankTransactionStatus.Error, InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        return BankTransactionStatus.Success, None

    def __eq__(self, other):
        if isinstance(other, BankAccount):
            return self.id == other.id
        return False

    def __str__(self):
        return f'{self.id}'

    def __hash__(self):
        return self.id.__hash__()
