import math
x, y = float(input()), float(input())
xc, yc, r = float(input()), float(input()), float(input())


def IsPointInCircle(x, y, xc, yc, r):
    a = x - xc
    b = y - yc
    nowR = math.sqrt(a ** 2 + b ** 2)
    return nowR <= r


if not IsPointInCircle(x, y, xc, yc, r):
    print('NO')
else:
    print('YES')
