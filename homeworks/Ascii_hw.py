# Write a for loop that prints the ASCII code of each character in a string named S. Use the built-in function ord(character) to convert each character to an ASCII integer (test it interactively to see how it works).

S = "I vowed I would always be yours Cause we survived the Great War"

for i in S:
    print(ord(i))

# Next, change your loop to compute the sum of the ASCII codes of all characters in a string.

result = 0
for i in S:
    result += ord(i)
print(result)

# Finally, modify your code again to return a new list that contains the ASCII codes of each character in the string. Does this expression have a similar effect—map(ord, S)?
# without map

ascii_list = []
for i in S:
    res = ord(i)
    ascii_list.append(res)
print(ascii_list)

# with map
change_S = list(S)

map_S = list(map(lambda x : ord(x), change_S))
print(map_S)



