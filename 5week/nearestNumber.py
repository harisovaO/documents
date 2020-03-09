n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
newList = []


def fun(numbers, target):
    return min(numbers, key=lambda x: abs(x - target))


print(fun(numbers, x))
