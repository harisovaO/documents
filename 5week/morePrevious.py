myList = list(map(int, input().split()))
for i in range(1, len(myList)):
    if myList[i] > myList[i - 1]:
        print(myList[i], end=' ')
