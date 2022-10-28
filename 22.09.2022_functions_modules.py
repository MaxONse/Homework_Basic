def sumOfN():
    a = int(input("Enter the 'N':"))
    b = a+a**2+a**3 # это если условие что n+n*n+n*n*n
    c = a+a*11+a*111 # а это если имелось ввиду 2+22+222
    print(b, c)
sumOfN()



def pairedNumbers():
    d = int(input("Enter first number:"))
    e = int(input("Enter second number, which bigger than first:"))
    for i in range(d, e+1):
        if not i % 2 and i != d and i != e:
            print(i)
pairedNumbers()