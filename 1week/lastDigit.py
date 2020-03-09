number = int(input())
arr = [number % 10, number // 10, number // 100,
       number // 1000, number // 10000]
print(arr[0])
