class Soda:
    def __init__(self, adder):
        if isinstance(adder, str):
            self.adder = adder
        else:
            self.adder = None

    def show_my_drink(self):
        if self.adder:
            print (f'Soda and {self.adder}')
        elif self.adder is None:
            print('Only Soda')


nothing = Soda(None)
some = Soda("Syrup")
something = Soda(18)

nothing.show_my_drink()
some.show_my_drink()
something.show_my_drink()


# ------------------------------------------------


class Nicola:
    def __init__(self, name, age):
        if name == 'Nicola':
            self.name = name
        else:
            self.name = f"I'm not {name}, I'm a Nicola"
        self.age = age


human = Nicola('John', 36)
human1 = Nicola('Nicola', 55)
print(human.name)
print(human1.name)