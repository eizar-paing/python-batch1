import re

def myanmar_ph(ph_num):
    phone_reg = "^[\+959][0-9]{8,12}+$"
    
    
    result = re.match(phone_reg, ph_num)

    if result:
        print("Your phone number is valid")
    else:
        print("Your phone number is invalid")

p1 = "+959449445366"
myanmar_ph(p1)

p2 = "+95955348833"
myanmar_ph(p2)

p3 = input("Enter your phone number dear: ")
myanmar_ph(p3)

# ^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$


