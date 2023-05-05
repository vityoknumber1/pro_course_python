from enum import Enum


class Curr(Enum):
    USD = 1
    UAH = 2
    EUR = 3
    GBP = 4

    def __str__(self):
        return self.name


exchange_rates = {
    Curr.USD: 1.0000,
    Curr.UAH: 36.5686,
    Curr.EUR: 0.905517,
    Curr.GBP: 0.79313,
}


class Price:
    def __init__(self, amount: float, currency: Curr) -> None:
        self.__amount: float = amount
        self.__currency: Curr = currency

    @property
    def amount(self) -> float:
        return self.__amount

    @property
    def currency(self) -> Curr:
        return self.__currency

    @amount.setter
    def amount(self, value: float) -> None:
        self.__amount = value

    def convert_cur(self, other_curr: Curr):
        price_in_usd = (
            self
            if Curr.USD == self.currency
            else Price(self.amount / exchange_rates[self.currency], Curr.USD)
        )
        return (
            price_in_usd
            if other_curr == price_in_usd.currency
            else Price(price_in_usd.amount * exchange_rates[other_curr], other_curr)
        )

    def __add__(self, other):
        if other is None:
            return self
        elif self is None and other is None:
            return None
        another = other
        if self.currency != other.currency:
            another = other.convert_cur(self.currency)
        return Price(self.amount + another.amount, self.currency)

    def __sub__(self, other):
        if other is None:
            return self
        elif self is None and other is None:
            return None
        another = other
        if self.currency != other.currency:
            another = other.convert_cur(self.currency)
        return Price(self.amount - another.amount, self.currency)

    def __str__(self):
        return f"{self.__amount:0.2f} {self.currency}"


def main() -> None:
    print(f"{Price(4.00, Curr.USD) + Price(100.00, Curr.USD)}")
    print(f"{Price(15.00, Curr.USD) + Price(36.5686, Curr.UAH)}")
    print(f"{Price(500.00, Curr.UAH) - Price(10.00, Curr.USD)}")


if __name__ == "__main__":
    main()
