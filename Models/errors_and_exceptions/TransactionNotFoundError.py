import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass
class TransactionNotFoundError(RuntimeError):
    time_stamp: datetime
    transaction_id: uuid
    bank_account_id: uuid
    message: str
    error_code: int

    def __init__(
            self,
            time_stamp: datetime,
            transaction_id: uuid,
            bank_account_id: uuid,
            message: str,
            error_code: uuid = -1
    ):
        super().__init__(
            f'Transaction `{transaction_id}` could not be found in bank account {bank_account_id} on {time_stamp}.\n'
            f'Message: {message}\n'
            f'Error Code: {error_code}')
        self.time_stamp = time_stamp
        self.transaction_id = transaction_id
        self.bank_account_id = bank_account_id
        self.message = message
        self.error_code = error_code
