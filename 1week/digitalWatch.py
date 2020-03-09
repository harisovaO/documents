number = int(input())
if (number // 60) >= 24:
    print((number // 60) % 24, number % 60)
else:
    print(number // 60, number % 60)
