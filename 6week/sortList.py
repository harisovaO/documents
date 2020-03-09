inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
myListNew = []
for line in inFile:
    myList = list(map(str, line.split()))
    myListNew.append(myList)
myListNewSort = sorted(myListNew)
for i in myListNewSort:
    i.pop(2)
    print(*i, file=outFile)
inFile.close()
outFile.close()
