number = int(input())
arr = [number % 10, (number % 100) // 10, number // 100]
print(arr[0] + arr[1] + arr[2])
