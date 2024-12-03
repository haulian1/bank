import uuid
from dataclasses import dataclass, field
from uuid import uuid4

from Models.Person import Person
from Models.Transaction import Transaction


@dataclass
class BankAccount:
    owner: Person
    balance: float
    account_id: uuid = uuid4()
    cur_transactions: list[Transaction] = field(default_factory=list)
    hist_transactions: dict[(int, int), list[Transaction]] = field(default_factory=dict)

    def __str__(self):
        return (f'{self.owner.full_name(include_middle=True, middle_initial=True)}'
                f'\nBalance: $ {self.balance}'
                # f'\nCurrent transactions: {[str(x) for x in self.cur_transactions]}'
                f'\nAccount ID: {self.account_id}'
                f'\nAddress: {self.owner.address.one_line()}')
