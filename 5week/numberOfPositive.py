myList = list(map(int, input().split()))
count = 0
for i in range(len(myList)):
    if myList[i] > 0:
        count += 1
print(count)
