import math


list_one = [32, 25, 15, 65, 42, 36, 28, -62, 0, 21, -13, 84, -45]
def summa(list_one):
    a = sum(list_one)
    print(a)
summa(list_one)

#---------------------------------------------------

def max_digit(list_one):
    max_number = max(list_one)
    print(max_number)
max_digit(list_one)

#----------------------------------------------------

def many(list_one):
    b = 0
    for i in list_one:
        if i%2 == 0:
            b += 1
    print("Paired numbers: ", b)
    c = 0
    for i in list_one:
        if i%2 != 0:
            c += 1
    print("Non paired numbers: ", c)
    d = 0
    e = 0
    f = 0
    for i in list_one:
        if i > 0:
            d += 1
        elif i < 0:
            e += 1
        else:
            f += 1
    print("Dodatni: ", d, "\n", "Vid'emni: ", e, "\n", "PaBHo Hyly: ", f)
many(list_one)

#---------------------------------------------

def perewertish(list_one):
    print(list(reversed(list_one)))
perewertish(list_one)

#---------------------------------------------

def finder():
    h = 28
    if h in list_one:
        print("28 founded in list!!!")
    else:
        print("Not found")
finder()

#---------------------------------------------

def factorial_numbers():
    list = []
    for i in list_one:
        if i > 0:
            k = math.factorial(i)
            list.append(k)
    print(list)
factorial_numbers()