n = int(input())
counts = 1
max = 1
i = 0
arr = []
while n != 0:
    arr.append(n)
    n = int(input())
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1]:
        counts += 1
        if counts > max:
            max = counts
    else:
        counts = 1
print(max)
