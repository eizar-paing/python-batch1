# Python program to sort list of dictionaries by values
def fun_dict1(x):
    return dict1[x]

dict1 = {"one": 3, "two": 5, "three": 2, "four": 1, "five": 4}
sorted_dict1 = sorted(dict1, key=fun_dict1)
print(sorted_dict1)

# Python program to extract dictionary with each key having non-numeric value from a given dictionary.
def getNonNumeric_Value(dict_val):
    non_numeric_dict = {}
    for key, val in dict_val.items():
        if not isinstance(val, (int, float)):
            non_numeric_dict[key] = val
    return non_numeric_dict

my_dict = {"one": "three", "two": 5, "three": 2, "four": "one", "five": 4}
result_dict = getNonNumeric_Value(my_dict)
print(result_dict)

# Python program to build a dictionary from list of two item (k,v) tuples.
list_tuple = [("a", 1), ("b", 2), ("c", 3), ("d", 4)]
dict3 = {}

for i in list_tuple:
    key = i[0]
    val = i[1]
    dict3[key] = val

print(dict3)

# Python program to merge two dictionary objects, using unpack operator.
dict4 = {"one": 3, "two": 5, "three": 2, "four": 1, "five": 4}
dict5 = {"six": "seven", "eight": 5, "nine": 2, "ten": "one", "five": 4}

def mergefun(d4, d5):
    result = {**d4, **d5}
    return result

merge_dict = mergefun(dict4, dict5)
print(merge_dict)