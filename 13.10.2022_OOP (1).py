class Auto:
    def __init__(self, model, year, manufacturer, engine, color, price):
        self.model = model
        self.year = year
        self.manuf = manufacturer
        self.engine = engine
        self.color = color
        self.price = price

    def __str__(self):
        return f'{self.model}, {self.year}, {self.manuf}, {self.engine}, {self.color}, {self.price}'

    def add_new(self, nmodel, nyear, nmanufacturer, nengine, ncolor, nprice):
        self.model = nmodel
        self.year = nyear
        self.manuf = nmanufacturer
        self.engine = nengine
        self.color = ncolor
        self.price = nprice


audi = Auto("100", "2001", "AUDI", "2,2", "RED", "4000")
bmw = Auto("328i", "2008", "BMW", "3,2", "BLACK", "8000")

print(audi)
print(bmw)


#-----------------------------------------------------------------

class Book:
    def __init__(self, name, year, publisher, genre, author, price):
        self.name = name
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self. author = author
        self.price = price

    def __str__(self):
        return f'{self.name}, {self.year}, {self.publisher}, {self.genre}, {self.author}, {self.price}'

    def add_new(self, nname, nyear, npublisher, ngenre, nauthor, nprice):
        self.name = nname
        self.year = nyear
        self.publisher = npublisher
        self.genre = ngenre
        self.author = nauthor
        self.price = nprice


mib = Book("Man In Black", "1999", "ACT, Terra Fantastica", "Fantasy", "Steve Perry", "399")
king = Book("11/22/63", "2012", "Hodder", "Fantasy", "Steven King", "310")

print(mib)
print(king)

#-------------------------------------------------------------------------------------

class Stadium:
    def __init__(self, name, date, country, loading):
        self.name = name
        self.date = date
        self.country = country
        self.loading = loading
    def __str__(self):
        return f'{self.name}, {self.date}, {self.country}, {self.loading}'

    def add_new(self, nname, ndate, ncountry, nloading):
        self.name = nname
        self.date = ndate
        self.country = ncountry
        self.loading = nloading

bb = Stadium("HNM", "11.01.2011", "USA", "40000")
dd = Stadium("PRD", "07.04.2001", "Germany", "80000")

print(bb)
print(dd)