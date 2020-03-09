x, y = float(input()), float(input())


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1


if not IsPointInSquare(x, y):
    print('NO')
else:
    print('YES')
