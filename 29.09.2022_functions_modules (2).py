def summary(arr):
    return sum(arr)


print(summary([12, 24, 3, 15, 16]))


# --------------------------------------


def minimum(x):
    return min(x)


print(minimum(x=[2, 5, 8, 1, 4]))

# -------------------------------------


def celoe(x):
    lst = 0
    for i in x:
        k = 2
        while k * k < i:
            if i % k == 0:
                break
            k += 1
        else:
            lst += 1
    print(lst)


celoe(x=[2, 5, 8, 9, 4, 6, 7])

#-------------------------------------------


def delete_starting_evens(lst):
    index = len(lst) - 1
    while index >= 0:
        if lst[index] % 2 == 0:
            lst.remove(lst[index])
        index -= 1
    return len(lst)


print(delete_starting_evens(lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#-------------------------------------------


def doubleList(u, n):
    return u+n


print(doubleList(u=[2, 4, 6, 8, 1], n=[9, 7, 5, 3]))


#-------------------------------------------


def stepen(b, m):
    h = []
    for a in b:
        j = a ** m
        h.append(j)
    print(h)


stepen(b=[1, 2, 3, 4, 5, 6], m=3)