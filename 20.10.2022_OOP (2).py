import math


class Money:
    def __init__(self, paper, change, currency):
        self.money = paper
        self.change = change
        self.currency = currency

    def __repr__(self):
        return f'{self.money}.{self.change}, {self.currency}'

    def sell(self, prod):
        if self.currency == prod.currency:
            if self.money > prod.money:
                g = (float(self.money + (float(self.change/100))) - (prod.money + (float(prod.change/100))))
                c = (g - (math.floor(g)))
                self.change = int(c * 100)
                self.money -= (math.floor(g))
                return "Sweet!!!"
            else:
                return "Find a job!!!"
        elif prod.currency == "USD":
            usd = prod.money * 36
            usdc = math.floor((prod.change * 36) / 100)
            usdcc = ((prod.change * 36) / 100) - usdc
            if self.money >= (usd + usdc):
                self.change = int(self.change - usdcc)
                self.money -= (usd + usdc)
                return "Sweet!!!"
            else:
                return "Find a job!!!"
        elif prod.currency == "EUR":
            eur = prod.money * 40
            ceur = math.floor((prod.change * 40) / 100)
            cceur = ((prod.change * 40) / 100) - ceur
            if self.money >= (eur + ceur):
                self.change = int(self.change - cceur)
                self.money -= (eur + ceur)
                return "Sweet!!!"
            else:
                return "Find a job!!!"


class Product(Money):
    def __init__(self, paper, change, currency, name):
        super().__init__(paper, change, currency)
        self.name = name
    pass


money = Money(100, 75, "UAH")
coffee = Product(1, 25, "EUR", "Coffee")
some = Product(35, 25, "UAH", "Espresso")
print(money)
print(money.sell(coffee))
print(money)
print(money.sell(some))
print(money)