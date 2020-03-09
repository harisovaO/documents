a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
determinant = a * d - b * c
if determinant != 0:
    determinant1 = e * d - b * f
    determinant2 = a * f - e * c
    x1 = determinant1 / determinant
    x2 = determinant2 / determinant
    print(x1, x2)
