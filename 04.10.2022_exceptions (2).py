def sum(b):
    a = '*'
    if b == 1:
        return a
    else:
        return a + sum(b-1)


print(sum(9))