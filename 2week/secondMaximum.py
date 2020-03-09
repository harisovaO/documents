n = int(input())
arr = []
while n != 0:
    arr.append(n)
    n = int(input())
arr.sort()
arr.pop()
arr.reverse()
print(arr[0])
