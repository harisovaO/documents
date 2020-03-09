inFile = open('input.txt', 'r', encoding='utf8')
gradePoint9, gradePoint10, gradePoint11 = 0, 0, 0
count9, count10, count11 = 1, 1, 1
sum9, sum10, sum11 = 0, 0, 0
for line in inFile:
    lineN = list(map(str, line.split()))
    if int(lineN[2]) == 9:
        n9 = int(lineN[3])
        sum9 += n9
        gradePoint9 = sum9 / count9
        count9 += 1
    if int(lineN[2]) == 10:
        n10 = int(lineN[3])
        sum10 += n10
        gradePoint10 = sum10 / count10
        count10 += 1
    if int(lineN[2]) == 11:
        n11 = int(lineN[3])
        sum11 += n11
        gradePoint11 = sum11 / count11
        count11 += 1
print(gradePoint9, gradePoint10, gradePoint11)
inFile.close()
