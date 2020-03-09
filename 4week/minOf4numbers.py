a, b = int(input()), int(input())
c, d = int(input()), int(input())


def min4(a, b, c, d):
    n1 = min(a, b)
    n2 = min(c, d)
    if n1 >= n2:
        print(n2)
    else:
        print(n1)


min4(a, b, c, d)
