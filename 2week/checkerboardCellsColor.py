a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a == c and abs(b - d) % 2 == 0) or \
        (b == d and abs(a - c) % 2 == 0) \
        or (abs(a - c) == abs(b - d)) or \
        (abs(a - c) % 2 == 0 and abs(b - d) % 2 == 0) or \
        (abs(a - c) % 2 != 0 and abs(b - d) % 2 != 0):
    print('YES')
else:
    print('NO')
