import uuid
from dataclasses import dataclass

from models.BankTransaction import BankTransaction

@dataclass
class UnknownTransactionTypeError(RuntimeError):
    destination_id: uuid
    transaction: BankTransaction
    error_code: int
    def __init__(self, dest_id: uuid, transaction: BankTransaction, error_code:int = -1):
        super().__init__(f'Unknown transaction type encountered and could not be processed.\n'
                         f'Destination is: {dest_id}\n'
                         f'Transaction is: {transaction}')
        self.destination_id = dest_id
        self.transaction = transaction
        self.error_code = error_code