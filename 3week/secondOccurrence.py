s = input()
sStart = s.find('f')
sEnd = len(s) - s[::-1].find('f') - 1
if sStart != -1:
    if sStart == sEnd:
        print(-1)
    else:
        nowS0 = s[0: sStart + 1]
        nowS1 = s[sStart + 1:]
        print(nowS1.find('f') + len(nowS0))
else:
    print(-2)
