import random
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = a + b


def merge(c):
    if len(c) <= 1:
        return c
    else:
        q = random.choice(c)
        l = []
        r = []
        m = []
        for elem in c:
            if elem < q:
                l.append(elem)
            elif elem > q:
                r.append(elem)
            else:
                m.append(elem)
        return merge(l) + m + merge(r)


print(*merge(c))
