# 1
# 22
# 333
# 4444
# 55555
# 666666S
# 7777777
# 88888888
# 999999999

for i in range(1, 10):  
    for j in range(i):
        print(i, end="")
    print()


# Trace
# Outer ==> 1
    # inner ==> 1
# Outer ==> 2
    # inner ==> 22
# Outer ==> 3
    # inner ==> 333
# Outer ==> 4
    # inner ==> 4444
        # ...
# Outer ==> 9
    # inner ==> 999999999


