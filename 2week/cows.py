number = int(input())
if number == 11 or number == 0 or 5 < number < 20 or \
        5 <= number % 10 <= 9 or number % 10 == 0:
    print(number, 'korov')
elif number % 10 == 1 or number == 1:
    print(number, 'korova')
else:
    print(number, 'korovy')
