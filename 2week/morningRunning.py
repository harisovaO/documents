x = int(input())
y = int(input())
a = x
i = 1
while a < y:
    a = a + a * 0.1
    i += 1
print(i)
