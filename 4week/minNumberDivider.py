import math
n = int(input())


def MinDivisor(n):
    i = 2
    while n % i != 0:
        if i >= math.sqrt(n):
            print(n)
            return
        i += 1
    print(i)


MinDivisor(n)
