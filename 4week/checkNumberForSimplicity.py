n = int(input())


def IsPrime(n):
    i = 2
    while i * i <= n and n % i != 0:
        i += 1
    return i * i > n


if not IsPrime(n):
    print('No')
else:
    print('YES')
