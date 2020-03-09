a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <= a or a + b + c <= 0:
    print('impossible')
elif b <= a >= c:
    result = a ** 2 - (c ** 2 + b ** 2)
    if result == 0:
        print('rectangular')
    elif result < 0:
        print('acute')
    elif result > 0:
        print('obtuse')
elif a <= b >= c:
    result = b ** 2 - (a ** 2 + c ** 2)
    if result == 0:
        print('rectangular')
    elif result < 0:
        print('acute')
    elif result > 0:
        print('obtuse')
else:
    result = c ** 2 - (a ** 2 + b ** 2)
    if result == 0:
        print('rectangular')
    elif result < 0:
        print('acute')
    elif result > 0:
        print('obtuse')

# if result == 0:
#     print('rectangular')
# elif result < 0:
#     print('acute')
# elif result > 0:
#     print('obtuse')