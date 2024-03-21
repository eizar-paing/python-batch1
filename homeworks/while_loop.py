# 1.   Repeatedly ask the user for their username and password until they enter the correct credentials (correct username and correct password).
# 2.   We want user to input any number between 100 and 500. Keep asking the user to enter a correct input until he/she enters the correct number within a given range.
#  3.   Write a while loop to display each character from a string and if a character is number then stop the loop.
#  4.   Print even and odd number between 1 to the number that user entered. 
# Eg. print(n, 'is a even number') or print(n, 'is a even number')
#  5.   Check how many times a given number can be divided by 3 before it is less than or equal to 10.

# for 1
print ("No.1")
username = "Susan"
password = "564789sv"

while True:
    user_username = input("Enter your username: ")
    user_password = input("Enter your password: ")

    if user_username == username and user_password == password:
        print("Welcome user!")
        break
    else: 
        print("Fail")

# for 2
print("No.2")

while True:
    user_num = int(input("Enter your number: "))

    if user_num > 100 and user_num < 500:
        print("Well done!")
        break
    else:
        print("Try again")

# for 3
print("No.3")

character = "Susan2Aung0"
total = 0

while total < len(character): # 0 < 11:
    i = character[total] # i = S
    if i.isdigit(): # i is dight?, No
        break 
    print(i) # S
    total += 1 # 1 = 0 + 1

# for 4
print("No.4")

user_number = int(input("Enter ypur number: "))
pass

    





    


