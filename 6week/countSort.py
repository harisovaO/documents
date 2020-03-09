myList = list(map(int, input().split()))


def CountSort(myList):
    emptyList = [0]*101
    for mark in myList:
        emptyList[mark] += 1
    for nowMark in range(101):
        print((str(nowMark) + ' ') * emptyList[nowMark], end='')
    return myList


CountSort(myList)
