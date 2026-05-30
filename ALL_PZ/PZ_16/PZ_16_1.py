# Практическое занятие №16, блок 1, вариант 15.
# Класс «Банк»: сумма денег, процентная ставка; начисление процентов и снятие.


class Bank:
    def __init__(self, balance=0.0, rate=0.0):
        self.balance = balance
        self.rate = rate

    def accrue_interest(self):
        """Процентные начисления на текущий остаток."""
        interest = self.balance * self.rate / 100
        self.balance += interest
        return interest

    def withdraw(self, amount):
        """Снятие денег при достаточном остатке."""
        if amount <= 0:
            raise ValueError('Сумма снятия должна быть положительной')
        if amount > self.balance:
            raise ValueError('Недостаточно средств на счёте')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError('Сумма пополнения должна быть положительной')
        self.balance += amount
        return self.balance

    def info(self):
        return f'Остаток: {self.balance:.2f} руб., ставка: {self.rate}%'


if __name__ == '__main__':
    bank1 = Bank(10000, 5)
    print(bank1.info())
    added = bank1.accrue_interest()
    print(f'Начислено процентов: {added:.2f}')
    print(bank1.info())
    bank1.withdraw(2000)
    print('После снятия 2000:', bank1.info())

    bank2 = Bank(5000, 10)
    print('\n', bank2.info())
    bank2.deposit(1500)
    bank2.accrue_interest()
    print('Второй счёт:', bank2.info())
