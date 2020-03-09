n = int(input())
counter = 0
while n != 0:
    if n % 2 == 0:
        counter += 1
    n = int(input())
print(counter)
