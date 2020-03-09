h = int(input())
a = int(input())
b = int(input())
path = 0
day = 1
while True:
    path = path + a
    if path >= h:
        break
    else:
        day = day + 1
        path = path - b
print(day)
