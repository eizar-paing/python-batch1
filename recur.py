def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        print('..... else')
        result = 0
    print(k)
    print('__________')
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
