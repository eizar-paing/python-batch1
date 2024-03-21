fruits = ["Apple", "Orange", "Grape"]
fruits.append("Berry")

# for i in fruits:
#     print(f'Fruit is : {i}')


# Break
for i in fruits:
    if i == "Apple":
        break
    print(f'Fruit is : {i}')

# Continue
for i in fruits:
    if i == "Orange":
        continue
    print(f'Fruit is : {i}')
print("hello")

# range(10)
# range(0, 10)

for i in range(10):
    print(f'i : {i}')

count = 0  # step 1
while count < len(fruits):
    if i == "Orange":
        break
    print(f'Fruit is : {fruits[count]}')  # fruits[2]
    count += 1
else:
    print('end of while loop')


for i in range(10):  # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(i)
for i in range(2, 10):  # 2, 3, 4, 5, 6, 7, 8, 9
    print(i)
for i in range(2, 10, 2):  # 2, 4, 6, 8
    print(i)
# count = 0
# while 0<4 => print(fruits[0])
# count = 0 + 1
# while 1<4 => print(fruits[1])
# count = 1 + 1
# while 2<4 => print(fruits[2])
# count = 2 + 1
# while 3<4 => print(fruits[3])
# count = 3 + 1
# while 4<4 => quit loop

# for(let i=0; i<10; i++ ) {

# }

# for i in range(10):
#     pass

number = int(input("Enter number: "))
# check the number is 0
i = 1
while i<=number: 
    if i%2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    i += 1

# need to solve
i = 1
while i>number:     # 1 > 5 (user input)
    if i%2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    i -= 1





# count = 0
# while count < 10:
#     print(f'Count: {count}')
#     count += 1 # count = count + 1

# else in for loop
for i in "apple":
    if i == "l":
        break
    print(i)
else:
    print("end of for loop")

# pass statement
for i in range(5):
    pass

# Nested loop
for i in range(5):  # outer loop
    for j in range(3):  # inner loop
        print(f'i is {i}, j is {j}')

# outer loop => i = 0,
# inner loop => j = 0, i is 0, j is 0
# => j = 1, i is 0, j is 1
# => j = 2, i is 0, j is 2
# outer loop => i = 1,
# inner loop => j = 0, i is 1, j is 0
# => j = 1, i is 1, j is 1
# => j = 2, i is 1, j is 2
# outer loop => i = 2,
# inner loop => j = 0, i is 2, j is 0
# => j = 1, i is 2, j is 1
# => j = 2, i is 2, j is 2

# ***
# ***
# ***
# ***
# ***

# for i in range(5):  # outer loop
#     for j in range(3):  # inner loop
#         print("*", end='')
#     print()

# *
# **
# ***
# ****
# *****
# ******
# *******

# 1
# 2
# 3
# 4
# 5


def pyramid_star(row_num):
    for i in range(1, row_num + 1):
        for j in range(i):
            print("*", end='')
        print()


rows = int(input("Enter row number: "))
pyramid_star(rows)


numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print(i*10)
