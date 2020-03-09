myList = list(map(int, input().split()))

for i in range(len(myList)):
    if myList[i] % 2 == 0:
        print(myList[i], end=' ')
