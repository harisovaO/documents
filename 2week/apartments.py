x = int(input())
y = int(input())
if (x - 1) % ((y + 1) - x) == 0:
    print('YES')
else:
    print('NO')
