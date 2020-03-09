s = input()
sStart = s.find('h')
sEnd = len(s) - s[::-1].find('h') - 1
nowS1 = s[0:sStart]
nowS2 = s[sEnd:]
nowS2r = nowS2[1:]
print(nowS1 + nowS2r)
