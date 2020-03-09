myList1 = set(list(map(int, input().split())))
myList2 = set(list(map(int, input().split())))
print(*sorted(myList1 & myList2))
