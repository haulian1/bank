class InsufficientFundsError(RuntimeError):
    balance: float
    withdrawal_amount: float
    error_code: int

    def __init__(self, balance: float, withdrawal_amount: float, error_code: int = -1):
        super().__init__(f'There were not enough funds to withdraw.'
                         f'Withdrawal amount: {withdrawal_amount} cannot be more than the balance: {balance}')
        self.balance = balance
        self.withdrawal_amount = withdrawal_amount
        self.error_code = error_code