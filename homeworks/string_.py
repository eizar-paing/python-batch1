# 1. Python program to sort the characters in a string

# 2. Python program to remove duplicate characters from a string

# 3. Python program to list unique characters with their count in a string

# 4. Python program to find number of words in a string

# 5. Python program to remove all non-alphabetic characters from a string

string = "Cause I'm in a field of dandelions Wishing on every one that you'd be mine, mine"

# No.1
print(sorted(string))

# No.2
new_str = []

for i in string:
    if i not in new_str:
        new_str.append(i)

remove_duplicate = "".join(new_str)
print(remove_duplicate)

# No.3
new_string = "We # were * too 1 close 2 to 3 the stars I 5 never knew 9 somebody 13 like you, somebody !!"




# No.4
count = 0

for i in new_string:
    if i.isalpha():
        count += 1

print(f"Number of words {count}")



# No.5
only_alpha = []

for i in new_string:
    if i.isalpha():
        only_alpha.append(i)

only_alpha_str = "".join(only_alpha)

print(only_alpha_str)