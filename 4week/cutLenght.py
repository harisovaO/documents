import math
x1, y1 = float(input()), float(input())
x2, y2 = float(input()), float(input())


def distance(x1, y1, x2, y2):
    print(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))


distance(x1, y1, x2, y2)
