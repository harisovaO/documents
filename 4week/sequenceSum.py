def sequence(sum):
    n = int(input())
    sum += n
    if n != 0:
        return sequence(sum)
    else:
        return sum

    # print("entering")
    # n = int(input())
    # sum += n
    # if n != 0:
    #     result = sequence(sum)
    #     print("from rescursive method ", result, "input", n)
    #     return result
    # else:
    #     result = sum
    #     print("result", result, "input", n)
    #     return result

    # while n != 0:
    #     n = int(input())
    #     sum += n
    # return sum


print(sequence(0))
