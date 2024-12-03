import uuid
from dataclasses import dataclass, field
from datetime import datetime

from Enums import Status
from Models.BankAccount import BankAccount
from Models.Person import Person
from Models.Transaction import Transaction


@dataclass
class Bank:
    owners: list[Person]
    date_established: datetime = datetime.now()
    total_assets: float = 0
    person_account_map: dict[uuid.UUID, list[BankAccount]] = field(default_factory=dict)
    cur_transactions: list[Transaction] = field(default_factory=list)
    hist_transactions: dict[(int, int), list[Transaction]] = field(default_factory=dict)

    def __post_init__(self):
        if len(self.person_account_map) > 0:
            for accounts in self.person_account_map.values():
                for account in accounts:
                    self.total_assets += account.balance

    def new_account(self, account: BankAccount):
        if not account.owner.person_id in self.person_account_map:
            self.person_account_map[account.owner.person_id] = []
        self.person_account_map[account.owner.person_id].append(account)
        self.update_assets()

    def search(self,
               current=True,
               historic=False,
               start: datetime = None,
               end: datetime = None,
               statuses: list[Status] = None):
        pass

    def cur_status(self) -> dict[Status, int]:
        cur_stats = {}
        for status in Status:
            cur_stats[status] = 0
        for transaction in self.cur_transactions:
            cur_stats[transaction.status] += 1
        return cur_stats

    def hist_status(self) -> dict[Status, int]:
        hist_stats = {}
        for status in Status:
            hist_stats[status] = 0
        for transaction in self.hist_transactions:
            hist_stats[transaction.status] += 1
        return hist_stats

    def all_status(self) -> dict[Status, int]:
        cur_stats = self.cur_status()
        hist_stats = self.hist_status()
        combined_stats = {}
        for status in Status:
            combined_stats[status] = cur_stats[status] + hist_stats[status]
        return combined_stats

    def update_assets(self, new_accounts = None, new_transactions = None, updated_transactions = None):
        self.total_assets = 0
        for person_accounts in self.person_account_map.values():
            for acc in person_accounts:
                self.total_assets += acc.balance


