myList = list(map(int, input().split()))
newMyList = []
i = 0
while i < len(myList):
    if len(myList) % 2 == 0:
        newMyList.append(myList[i + 1])
        newMyList.append(myList[i])
        i += 2
    else:
        if (i + 1) >= len(myList) - 1:
            newMyList.append(myList[(i - 1) + 1])
            break
        newMyList.append(myList[i + 1])
        newMyList.append(myList[i])
        i += 2

print(*newMyList)
