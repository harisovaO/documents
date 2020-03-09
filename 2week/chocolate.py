n = int(input())
m = int(input())
k = int(input())
if (k == n or k == m or k % m == 0 or k % n == 0) \
        and k <= n * m:
    print('YES')
else:
    print('NO')
