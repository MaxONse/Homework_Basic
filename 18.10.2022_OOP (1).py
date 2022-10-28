import math


class Device:
    def __init__(self, ids, power, size, price, color):
        self.ids = ids
        self.power = power
        self.size = size
        self.price = price
        self.color = color

    def __repr__(self):
        return "OK"


class CoffMachine(Device):
    def __init__(self, ids, power, size, price, color, typeof, subtype):
        super().__init__(ids, power, size, price, color)
        self.typeof = typeof
        self.subtype = subtype

    def __repr__(self):
        return f'{self.typeof}, {self.subtype}, {self.color}, {self.power}, {self.size}, {self.ids}'


class Blender(Device):
    def __init__(self, ids, power, size, price, color, typeof, subtype):
        super().__init__(ids, power, size, price, color)
        self.typeof = typeof
        self.subtype = subtype

    def __repr__(self):
        return f'{self.typeof}, {self.subtype}, {self.color}, {self.power}, {self.size}, {self.ids}'


class MeatGrinder(Device):
    def __init__(self, ids, power, size, price, color, typeof, subtype):
        super().__init__(ids, power, size, price, color)
        self.typeof = typeof
        self.subtype = subtype

    def __repr__(self):
        return f'{self.typeof}, {self.subtype}, {self.color}, {self.power}, {self.size}, {self.ids}'


# --------------------------------------------------------------------------------------------------


class Ship:
    def __init__(self, mass, shwidth, shheight, shlenght, speed):
        self.mass = mass
        self.width = shwidth
        self.height = shheight
        self.lenght = shlenght
        self.speed = speed

    def __repr__(self):
        return f'Good'


class Frigate(Ship):
    def __init__(self, typeof, weapons, mass, shwidth, shheight, shlenght, speed):
        super().__init__(mass, shwidth, shheight, shlenght, speed)
        self.typeof = typeof
        self.weapons = weapons

    def __repr__(self):
        return f'{self.typeof}, {self.weapons}, {self.mass}, {self.width}, {self.lenght}, {self.height}, {self.speed}'


class Destroyer(Ship):
    def __init__(self, typeof, weapons, mass, shwidth, shheight, shlenght, speed):
        super().__init__(mass, shwidth, shheight, shlenght, speed)
        self.typeof = typeof
        self.weapons = weapons

    def __repr__(self):
        return f'{self.typeof}, {self.weapons}, {self.mass}, {self.width}, {self.lenght}, {self.height}, {self.speed}'


class Cruiser(Ship):
    def __init__(self, typeof, weapons, mass, shwidth, shheight, shlenght, speed):
        super().__init__(mass, shwidth, shheight, shlenght, speed)
        self.typeof = typeof
        self.weapons = weapons

    def __repr__(self):
        return f'{self.typeof}, {self.weapons}, {self.mass}, {self.width}, {self.lenght}, {self.height}, {self.speed}'


# ------------------------------------------------------------------------------------------------------------------

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
            #     if self.change < prod.change:
            #         self.money -= 1
            #         self.change += 100
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