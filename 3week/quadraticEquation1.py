import math
a, b, c = float(input()), float(input()), float(input())
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    arr = [x1, x2]
    arr.sort()
    print(arr[0], arr[1])
elif d == 0:
    x1 = x2 = -b / (2 * a)
    if x1 == 0:
        print(abs(x1))

    else:
        print(x1)
