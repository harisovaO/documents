myList = open('input.txt', 'r', encoding='utf-8')
outFile = open('output.txt', 'w', encoding='utf-8')
newList = []
newListJoint = []
listPast = []
listDropout = []
listDropoutSum = []
passingScore = 0
countDropout = 0
countPast = 0
k = int(myList.readline())
for line in myList:
    lineN = list(map(str, line.split()))
    newList.append(lineN)
# for i in newList:
#     newListJoint.append(int(i[-3]) + int(i[-2]) + int(i[-1]))
# newListJointSort = sorted(newListJoint, reverse=True)
# print(newListJointSort)
# pastEnd = newListJointSort[:k:]
# print(pastEnd)
for i in newList:
    if int(i[-3]) <= 40 or int(i[-2]) <= 40 or int(i[-1]) <= 40:
        listDropout.append(int(i[-3]))
        listDropout.append(int(i[-2]))
        listDropout.append(int(i[-1]))
        listDropoutSum.append(int(i[-3]) + int(i[-2]) + int(i[-1]))
        countDropout += 1
    else:
        listPast.append(int(i[-3]) + int(i[-2]) + int(i[-1]))
# print('listDropoutSum= ', listDropoutSum, 'listPast= ', listPast,
#       'countDropout= ', countDropout)
listDropoutSum.append(countDropout)

listCommon = listPast + listDropoutSum
listCommon.pop(-1)
listCommonSort = sorted(listCommon, reverse=True)
listCommonSlice = listCommonSort[:k:]
print('listCommonSort= ', listCommonSort, 'listCommonSlice= ', listCommonSlice)
print('длина listCommon ', len(listCommon) - 1)
for i in listDropoutSum:
    if countDropout != 0 and listPast == []:
        print('0')
        break
    if k == 0 or (len(listCommon) - 1 == k and countDropout != 0):
        print('0')
listDropoutSum.pop(countDropout)
listK = sorted(listPast, reverse=True)
listSlice = listK[:k:]
# print('listSlice срезанный', listSlice, 'listK сорт', listK)
if len(listSlice) == 1:
    if listSlice[0] == listK[0]:
        print('1')
if len(listSlice) > 1:
    for i in range(len(listSlice) - 1):
        if listSlice[i] == listSlice[i + 1]:
            countPast += 1
            continue
        if countPast > k:
            print('1')
            break

        elif len(listCommonSlice) != len(listCommonSort):
            if listCommonSort[len(listCommonSlice) - 1] == listCommonSort[len(listCommonSlice)] and k > 2:
                print(listCommonSort[len(listCommonSlice) - 2])
                break
            else:
                print(listCommonSort[k - 1])
                break
        # elif len(listSlice) != len(listK):
        #     if listK[len(listSlice) - 1] == listK[len(listSlice)] and k > 2:
        #         print(listK[len(listSlice) - 2])
        #         break
        #     else:
        #         print(listK[k - 1])
        #         break
myList.close()
outFile.close()
