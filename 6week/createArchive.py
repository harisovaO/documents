s_n = list(map(int, input().split()))
maxAmount = s_n[0]
maxNumberOfUser = s_n[1]
count, summer = 0, 0
newList = []
i = 0
while i < maxNumberOfUser:
    newList.append(int(input()))
    i += 1
newList.sort()
for i in newList:
    if i <= maxAmount:
        summer += i
        if summer <= maxAmount:
            count += 1
    else:
        continue
print(count)
