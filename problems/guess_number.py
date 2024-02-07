# Create a variable called compnum and set the value to 50.
# Ask the user to enter a number. While their guess is not the same as the compnum value,
# tell them if their guess is too low or too high and ask them to have another guess.
# If they enter the same value as compnum, display the message “Well done,
# you took [count] attempts”

compnum = 50
count = 0
num = 0
while num != compnum:  # 50 != 50 => false
    num = int(input("guess number: "))
    count += 1
    if num == compnum:  # should be first to break as soon as it gets correct number
        print("Well done")
        break
    elif num > compnum:
        print("too high")
    else:
        print("too low")
print(count)
