a1, b1, c1 = int(input()), int(input()), int(input())
a2, b2, c2 = int(input()), int(input()), int(input())
v1 = a1 * b1 * c1
v2 = a2 * b2 * c2
arr1 = [a1, b1, c1]
arr1.sort()
arr2 = [a2, b2, c2]
arr2.sort()
if arr1 == arr2:
    print('Boxes are equal')
elif arr1[0] <= arr2[0] and arr1[1] <= arr2[1] and arr1[2] <= arr2[2]:
    print('The first box is smaller than the second one')
elif arr1[0] >= arr2[0] and arr1[1] >= arr2[1] and arr1[2] >= arr2[2]:
    print('The first box is larger than the second one')
else:
    print('Boxes are incomparable')
