myList = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
newMyList = []
stringsInt = []
for line in myList:
    lineN = list(map(str, line.split()))
    # print(*lineN, file=outFile)
    newMyList.append(lineN)
newMyList.pop(0)
minimum = 0
sortedList = sorted(newMyList, key=lambda newMyList: int(newMyList[1]),
                    reverse=True)
for line in sortedList:
    print(line[0])
myList.close()
outFile.close()
