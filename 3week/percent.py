p, x, y = int(input()), int(input()), int(input())
cop = float('{0:.6f}'.format(y * 0.01))
deposit = float(x + cop)
percent = deposit * p/100
nowDeposit = float(deposit + percent)
nowCop = float('{0:.6f}'.format(nowDeposit - int(nowDeposit)))
nowCop2 = int(nowCop * 100)
print(int(nowDeposit), nowCop2)
