a1 = int(input())
b1 = int(input())
c1 = int(input())

a2 = int(input())
b2 = int(input())
c2 = int(input())

hour1 = a1 * 3600
minute1 = b1 * 60

hour2 = a2 * 3600
minute2 = b2 * 60

res = hour2 + minute2 + c2 - (hour1 + minute1 + c1)
if res < 0:
    print(-1 * res)
else:
    print(res)

