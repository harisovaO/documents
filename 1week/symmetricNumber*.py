import random
a = int(input())
if a // 1000 == a % 10 and (a % 1000) // 100 == (a % 100) // 10:
    print(1)
else:
    print(random.randint(2, 1000))

