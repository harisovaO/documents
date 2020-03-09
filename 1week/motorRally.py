n = int(input())
m = int(input())
res = m // n
if m % n != 0:
    print(res + 1)
else:
    print(res)

