from dataclasses import dataclass


@dataclass
class Currency:
    currency_symbol: str
    whole_amount: str = '0'
    fractional_amount: str = '0'
    separator: str = ','
    decimal_symbol: str = '.'

    def __eq__(self, other):
        if isinstance(other, Currency):
            return self.currency_symbol == other.currency_symbol \
                and self.whole_amount == other.whole_amount \
                and self.fractional_amount == other.fractional_amount \
                and self.separator == other.separator \
                and self.decimal_symbol == other.decimal_symbol
        return False

    def __str__(self):
        return f'{self.currency_symbol} {self.whole_amount}.{self.fractional_amount}'

    def __hash__(self):
        return hash((self.currency_symbol, self.whole_amount, self.fractional_amount))

    def __add__(self, other):
        if isinstance(other, Currency):
            pass
        if isinstance(other, int):
            pass
        if isinstance(other, float):
            pass
        raise NotImplementedError

    def __radd__(self, other):
        if isinstance(other, int):
            pass
        if isinstance(other, float):
            pass
        return NotImplementedError
