s = input()
separatorIndex = s.find(' ')
nowS1 = s[0: separatorIndex]
nowS2 = s[separatorIndex + 1:]
print(nowS2, nowS1)
