a, n = float(input()), int(input())


def powers(a, n):
    if n == 0:
        return 1
    if n == -1:
        return 1 / a
    fun = powers(a, n // 2)
    fun *= fun
    if n % 2:
        fun *= a
    return fun


print(powers(a, n))
