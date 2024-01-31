x = 10
y = 20

# if condition
if x < y:  # true
    print('x is less than y.')

# if/else condition
if x < y:  # true
    print('x is less than y.')
else:  # false
    print('y is greater than x.')

# elif condition
if x < y:
    print('x is less than y.')
elif x == y:
    print('x is equal to y.')
else:
    print('x is greater than y.')

# nested if
if x < y:
    if x*2 == y:
        if x % 2 == 0:
            print('x is double of y and it is even.')
        else:
            print('x is double of y and it is odd.')
    else:
        print('x is less then y but not double')

# Logical operators ( and , or , not)
# and
if x > 0 and x < 100:  # x = 101
    print('x is between 0 and 100.')

# or
if x > 0 or x < 10:
    print(x > 0 or x < 10)  # true or false

# not
if not (x == y):  # not(false) => true /  not(true) => false
    print('x is not equal to y.')
# else:
#     print('x is equal to y.')

if x == y:
    print('x is equal to y.')
else:
    print('x is not equal to y.')

# in
numbers = [1, 2, 3, 4]
if x in numbers:
    print(x in numbers)
else:
    print(x in numbers)

# not in
if x not in numbers:
    print(f'true case {x not in numbers}')
else:
    print(f'false case {x not in numbers}')

# is
if x is y:  # 2 is 2 => true
    print(f'equal case {x is y}')
else:
    print(f'not equal case {x is y}')

# is not
if x is not y:  # 2 is not 2 => false
    print(f'not equal case {x is not y}')
# else:
#     print(f'equal case {x is not y}')

# and
# true and true => true
# true and false => false
# false and false => false

# or
# true or true => true
# true or false => true
# false or false => false
