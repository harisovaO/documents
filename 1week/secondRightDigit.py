number = int(input())
arr = [number % 10, (number % 100) // 10, number // 100,
       number // 1000, number // 10000]
if number < 10:
    print(0)
else:
    print(arr[1])
