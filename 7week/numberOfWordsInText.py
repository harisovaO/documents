# from sys import stdin
# inFile = stdin.readlines
import re
inFile = open('input.txt', 'r', encoding='utf8')
lines = str(inFile.readlines())
# words = lines.replace(';', ' ').split()
# print(words)
newLines = re.split(r', |_|-|!', lines)
# print(newLines)
myList = set()
# count = 0
for elem in newLines:
    myList.add(elem)
print(myList)

punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']
wordList = lines.split()

inFile.close()


# re.split('(\W+)', 'Words, words, words.')