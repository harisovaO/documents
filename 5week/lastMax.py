from operator import itemgetter
myList = list(map(int, input().split()))


def lastMax(myList):
    return max(enumerate(myList), key=itemgetter(1, 0))[::-1]


resFun = lastMax(myList)
print(resFun[0], resFun[1])
