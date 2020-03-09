a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abs(a - c) == 1 and abs(b - d) == 1 or a == c and\
        abs(b - d) == 1 or b == d and abs(a - c) == 1:
    print('YES')
else:
    print('NO')
