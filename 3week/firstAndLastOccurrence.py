s = input()
sStart = s.find('f')
sEnd = len(s) - s[::-1].find('f') - 1
if sStart != -1:
    if sStart == sEnd:
        print(sStart)
    else:
        print(sStart, sEnd)
