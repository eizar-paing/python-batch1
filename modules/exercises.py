numbers = [2, 5, 7, 10, 15, 18, 20, 85, 100, 123, 155, 525, 550]
result = [5, 10, 15, 20, 85, 100]

# question 1
# numbers must be divisible by 5.
# if the number is greater than 150, skip it, move to the next number
# if the number is greater than 500, stop the loop.

for i in numbers:
    if i > 500:
        break
    if i > 150:
        continue
    if (i % 5 == 0):
        print(i)

print(numbers)

# question 2
# fibonacci sequence:   0     1     1     2 3 5 8 ....
# num1  num2  num3
#       num1  num2  num3


def get_fibonacci(num1, num2):
    result = str(num1) + ", " + str(num2)
    for i in range(10):
        num3 = num1 + num2
        result += ", " + str(num3)
        num1 = num2
        num2 = num3
    print(result)


# question 3
# factorial => 5! = 5 * 4 * 3 * 2 * 1 = 120
# 5! => 1 * 2 * 3 * 4 * 5 = 120
# factorial of 3 = 3! = 1 * 2 * 3 = 6
res = 1
for i in range(1, 6):
    res = res * i
print(res)
