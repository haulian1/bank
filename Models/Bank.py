import uuid
from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4

from models.BankAccount import BankAccount
from models.BankTransaction import BankTransaction
from models.Enums import BankTransactionStatus
from models.Person import Person


@dataclass
class Bank:
    accounts: dict[uuid, BankAccount]
    account_holders: dict[uuid, Person]
    personal_accounts: dict[uuid, list[BankAccount]]
    current_transactions: dict[datetime, list[BankTransaction]]
    historic_transactions: dict[(int, int), dict[datetime, list[BankTransaction]]]
    bank_owners: list[Person]
    bank_id: uuid = uuid4()

    def upsert_transaction(self, time_stamp:datetime, transaction: BankTransaction) -> None:
        if time_stamp not in self.current_transactions:
            self.current_transactions[time_stamp] = []
        self.current_transactions[time_stamp].append(transaction)

    def get_year_month(self, time_stamp: datetime) -> (int, int):
        return time_stamp.year, time_stamp.month

    def move_records_to_history(self) -> None:
        for time_stamp, bank_transactions in self.current_transactions:
            historic_key = self.get_year_month(time_stamp)
            if historic_key not in self.historic_transactions:
                self.historic_transactions[historic_key] = {}

            if time_stamp not in self.historic_transactions[historic_key]:
                self.historic_transactions[historic_key][time_stamp] = []

            self.historic_transactions[historic_key][time_stamp].extend(bank_transactions)

    def open_account(self, owner: list[Person], initial_balance: float) -> uuid:
        current_time = datetime.now()

        new_account = BankAccount(owner, initial_balance)

        transaction = BankTransaction(
            None,
            new_account.id,
            initial_balance,
            BankTransactionStatus.Initiated
        )

        transaction = new_account.process_transaction(current_time, transaction)

        if len(transaction.errors) > 0:
            self.handle_transaction_errors(transaction.errors)
            return None

        self.accounts[new_account.id] = new_account

        for person in new_account.owner:
            self.account_holders[person.id] = person
            if person.id not in self.personal_accounts:
                self.personal_accounts[person.id] = []
            self.personal_accounts[person.id].append(new_account)

        return new_account.id

    def handle_transaction_errors(self, errors: list[(datetime, Exception)]):
        pass
