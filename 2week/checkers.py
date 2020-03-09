a, b = int(input()), int(input())
c, d = int(input()), int(input())
one = (a + b) % 2
two = (c + d) % 2
if one == two and a * b <= c * d:
    print('YES')
else:
    print('NO')

