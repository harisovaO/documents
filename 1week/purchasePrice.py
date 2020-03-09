a = int(input())
b = int(input())
n = int(input())
priceRub = a * n
priceCop = b * n
if priceCop >= 100:
    print(priceRub + priceCop // 100, priceCop % 100)
else:
    print(priceRub, priceCop)
