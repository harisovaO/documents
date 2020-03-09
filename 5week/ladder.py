n = int(input())
arr = [n]
arr.pop(0)
for i in range(1, n + 1):
    str(arr.append(i))
    # print(arr)
    print("".join(map(str, arr)))
