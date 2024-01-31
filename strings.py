# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Smith'
age = 37


# Concatenate
print('Hello, my name is ' + name + ' and I am ' + str(age) + '.')


# 'Hello, my name is Brad and I am 37.'

# String Formatting

# Arguments by position
print('My name is {n} and I am {a}'.format(n=name, a=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name} and I am {age}')

# String Methods

s = 'Hello world2'
# S = 'Helloworld3'

# Capitalize string
print(s.capitalize())
# print(S.upper())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
char = 'h'
print(s.count(char))

# Starts with
print(s.startswith('Hello'))

# Ends with
print(s.endswith('d'))

# Split into a list
print(s.split())

# Find position
print(s.find('r'))  # 8

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())
