n = int(input()) #кол-во селений
numberN = list(map(int, input().split())) #расстояние от начала дороги до i-го селения
m = int(input()) #кол-во бомбоубежищ
numberM = list(map(int, input().split())) #расст. от начала дороги до i бомбоубежища
results = []


def ListTuples(tuples):
    tuples = [list((tuples[i], i)) for i in range(len(tuples))]
    # print('изначально: ', tuples)
    tuples.sort(key=lambda tup: tup[0])
    return tuples


tuplesN = ListTuples(numberN)
tuplesM = ListTuples(numberM)
print(tuplesN)
print(tuplesM)
# print(tuplesM[0][1])
# newTuples = [list((i + 1, tuplesN[i])) for i in range(len(tuplesN))]

newTuplesProb = []
value = []
listToInsert = []
for i in tuplesN:
    # print(i)
    if len(tuplesM) == 1:
        newTuplesProb.append(i[1] + 1)
    else:
        for j in range(len(tuplesM)):
            value.append(abs(i[0] - int(tuplesM[j][0])))
        print(value)
        # for a in value:
        #     if a < value:
        # for n in range(len(value) + 1):
        #     if value[n] <= value[n + 1]:
        #         listToInsert.append(n)
print(listToInsert)
print(newTuplesProb)

# min = 0
# difference = []
# for i in tuplesN:
#     for j in range(len(tuplesM)):
#         val = abs(i[1] - tuplesM[j][1])
#         difference.insert(val, i)
        # difference.append(val)
        # print(difference)

# print(difference)


# 4
# 6 10 1 2
# 2
# 7 3
# listLocations = []
# listBombs = []
# j, k, p, z = 0, 0, 0, 0
# for i in range(n):
#     if j < len(numberN):
#         listLocations.append([numberN[j], i])
#         j += 1
# for i in range(m):
#     if k < len(numberM):
#         listBombs.append([numberM[k], i])
#         k += 1
# listLocations.sort()
# listBombs.sort()
# # print(*listLocations)
# # print(*listBombs)
# newListLocations = []
# newListBombs = []
# for i in range(len(listBombs)):
#     newListBombs.append(listBombs[i][1])
# for i in range(len(listLocations)):
#     if z < len(newListBombs):
#         newListLocations.append([listLocations[z], newListBombs[z] + 1])
#     z += 1
# # print(*newListLocations)
# # print(newListLocations[0][0][1], newListLocations[1][0][1], newListLocations[2][0][1])
# newListLocations.sort(key=lambda tup: tup[0][1])
# # print(*newListLocations)
# for i in range(len(newListLocations)):
#     print(newListLocations[i][1], end=' ')