n = int(input())
arr = []
max = n
while n != 0:
    arr.append(n)
    if n > max:
        max = n
    n = int(input())
print(arr.count(max))
