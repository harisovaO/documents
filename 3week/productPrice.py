import math
n = float(input())
cop = float('{0:.2f}'.format((n % 1) * 100))
rub = int(n)
print(rub, int(cop))
