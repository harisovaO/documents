myList = list(map(int, input().split()))
minimum = min(myList)
maximum = max(myList)
newMyList = []
for i in myList:
    if i == minimum:
        minimum = i
        newMyList.append(maximum)
    elif i == maximum:
        maximum = i
        newMyList.append(minimum)
    else:
        newMyList.append(i)

print(*newMyList)
