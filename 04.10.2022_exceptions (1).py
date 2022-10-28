def degree(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * degree(a, b - 1))

print(degree(a=2, b=5))