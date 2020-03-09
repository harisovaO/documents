abc = [int(input()), int(input()), int(input())]
de = [int(input()), int(input())]
abc.sort()
de.sort()
if abc[0] <= de[0] and abc[1] <= de[1]:
    print('YES')
else:
    print('NO')
