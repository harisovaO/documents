n, m = int(input()), int(input())


def ReduceFraction(n, m):
    nod = m % n
    if nod == 0:
        return n
    else:
        return ReduceFraction(nod, n)


nod = ReduceFraction(n, m)
print(n // nod, m // nod)
