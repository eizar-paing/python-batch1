rows = int(input("Enter the number of rows:"))

val = rows - 1
for i in range(rows):
    for j in range(rows):
        if (i == 0 or i == val or j == 0 or j == val):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
