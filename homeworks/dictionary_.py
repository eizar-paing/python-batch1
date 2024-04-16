# Python program to sort list of dictionaries by values
def fun_dict1(x):
    return dict1[x]

dict1 = {"one": 3, "two": 5, "three": 2, "four": 1, "five": 4}
sorted_dict1 = sorted(dict1, key=fun_dict1)
print(sorted_dict1)

# Python program to extract dictionary with each key having non-numeric value from a given dictionary.
dict2 = {"one": "three", "two": 5, "three": 2, "four": "one", "five": 4}
new_dict2 = {}

for k,v in dict2.items():
    if not v.isnumeric():
        new_dict2[k] = v  
print(new_dict2)


# Python program to build a dictionary from list of two item (k,v) tuples.

# Python program to merge two dictionary objects, using unpack operator.

