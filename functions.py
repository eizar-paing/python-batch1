def print_hello(name):  # parameter
    print("Hello ", name)
    print('Good morning')


print_hello("John")  # argument
print_hello("Smith")
print_hello("Merry")


def add(num1, num2):  # 2 parameters
    result = num1 + num2


def adds(**nums):  # arbitrary keyword arguments
    result = 0
    for i in nums:
        result += nums[i]
    print(result)


def arb_add(*nums):
    result = 0
    for i in nums:
        result += i
    print(result)


add(num2=2, num1=1)  # 2 arguments # keyword arguments
add(1, 2)  # position arguments

adds(n1=1, n2=2, n3=3)
adds(n1=1, n2=2, n3=3, n4=4, n5=5)

arb_add(1, 2, 3, 4)
arb_add(2, 3, 4, 5, 6, 7)
