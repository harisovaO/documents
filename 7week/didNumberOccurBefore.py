myList = list(map(int, input().split()))
newMyList = set()
for elem in myList:
    if elem in newMyList:
        print("YES")
    else:
        print("NO")
    newMyList.add(elem)
