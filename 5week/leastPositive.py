myList = list(map(int, input().split()))
newMyList = []
for i in myList:
    if i > 0:
        newMyList.append(i)
minimum = newMyList[0]
for i in newMyList:
    if i < minimum:
        minimum = i
print(minimum)
