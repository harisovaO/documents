n = int(input())
strings1 = "+___ "
strings2 = "|" + str(n) + " / "
strings3 = "|__\\ "
strings4 = "|    "
count = 1
arr = [strings1, strings2, strings3, strings4]
for i in arr:
    for j in range(1, n + 1):
        if arr[1] == i:
            # i = " |" + str(j) + " / "
            print("|" + str(j) + " / ", end='')
        else:
            print(i, end='')
    count += 1
    print()
