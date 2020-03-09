n = int(input())
minute = (n // 60) % 60
sec = n % 60
if minute < 10:
    minute = '0' + str(minute)
if sec < 10:
    sec = '0' + str(sec)
print(((n // 60) // 60) % 24, minute, sec, sep=':')
