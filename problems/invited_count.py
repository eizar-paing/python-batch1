count = 0
next = 'yes'

while next == 'yes':
    count += 1
    name = input("Enter name you want to invited: ")
    print("you already invited ", name)
    next = input("Do you want to next person: ")
print("Total number of people you invited is ", count)
