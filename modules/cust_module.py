def pyramid_star(row_num):
    for i in range(1, row_num + 1):
        for j in range(i):
            print("*", end='')
        print()


def new_fun():
    print("new function of custom module ")


def add(*nums):
    result = 0
    for i in nums:
        result += i
    return result


def multiply(*nums):
    result = 1
    for i in nums:
        result *= i
    return result
