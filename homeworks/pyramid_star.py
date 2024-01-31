
#      *     # 4 space
#     ***    # 3 space
#    *****   # 2 space
#   *******  # 1 space
#  ********* # 0 space

print('start of for loop')
for i in range(5):
    for space in range(5-i-1):
        print(' ', end='')
    for j in range(1, 2*i+2):
        print('*', end='')
    print()

# rows = 5
# for space
# i = 0 => space = 4
# i = 1 => space = 3
# i = 2 => space = 2
# i = 3 => space = 1
# i = 4 => space = 0
# space = rows - i - 1

# for star
# i = 0 => j = 1 , 0
# i = 1 => j = 3 , 2
# i = 2 => j = 5 , 4
# i = 3 => j = 7 , 6
# i = 4 => j = 9 , 8
# j = 2*i + 1

# example of iq test
# 1, 2, 3, 4 => i
# 5, 10, 15, 20  => j = 5*i

# Trace of testing code
# outer loop, i=0
#     inner loop => j = 1, (1, 0) quit
# print()

# outer loop, i=1
#     inner loop => j = 1, (1, 1) quit
# print()

# outer loop, i=2
#     inner loop => j = 1,  (1, 2) => print('* ', end='')
#                   j = 3, (1, 2) => quit
# print()

# outer loop, i=3
#     inner loop => j = 1,  (1, 3) => print('* ', end='')
#                   j = 3, (1, 3) => quit
# print()


# outer loop, i=3
#     inner loop => j = 1,  (1, 3) => print('* ', end='')
#                   j = 3, (1, 3) =>  quit
# print()

# outer loop, i=4
#     inner loop => j = 1,  (1, 4) => print('* ', end='')
#                   j = 3, (1, 4) => print('* ', end='')
#                   j = 5, (1, 4) => quit
# print()
