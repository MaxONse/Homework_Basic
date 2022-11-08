import math
def formatted_text():
    text = (" Don’t compare yourself with anyone in this world… if you do so, you are insulting yourself")
    author = "Bill Gates"
    probel = ' '
    halftext = text.split()
    first = math.ceil((len(halftext)//2))
    print('"', " ".join(halftext[:first]), "\n", " ".join(halftext[first:]),'"', "\n", 39*probel, author)
formatted_text()

#---------------------------------------------------------------------------------------------------------

def paired(num1, num2):
    k = []
    for i in range(num1, num2+1):
        if i%2 == 0:
            k.append(i)
    print(k)
paired(num1 = 1, num2 = 17)

#--------------------------------------------------------------------------------------------------------

def square(sum, n, fill=True):
    line = n * sum
    if fill:
        for _ in range(n):
            print(line)
    else:
        print(line)
        for _ in range(n - 2):
            print(sum + " " * (n - 2) + sum)
        print(line)


square("*", 5, True)

#---------------------------------------------------------------------------------------------------------

def minimum(x):
    print(min(x))
minimum(x=[2, 5, 8, 1, 4])

#---------------------------------------------------------------------------------------------------------

def dobutok(a, b):
    if a == b:
        return "Error"
    elif a > b:
        a, b = b, a
    h = 1
    for i in range(a, b + 1):
        h *= i
    return h
print(dobutok(5, 25))

#--------------------------------------------------------------------------------------------------------

def sum_digits(d):
    k = 0
    for i in  range(len(str(d))):
        k += 1
    return k
print(sum_digits(7653808))

#-------------------------------------------------------------------------------------------------------

def yjac(x):
    revers = ''.join(reversed(str(x)))
    return str(x) == str(revers)
print(yjac(1551))