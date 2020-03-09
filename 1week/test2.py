number = int(input())
arr = ['    _~_    ', '   (o o)   ', '  /  V  \  ',
       ' /(  _  )\ ', '   ^^ ^^   ']
for i in arr:
    for a in range(number):
        print(i, end='')
    print()
