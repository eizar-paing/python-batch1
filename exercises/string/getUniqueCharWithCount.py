#Python program to list unique characters with their count in a string

mystr = "HelloWorld"
# result = {"H": 1, "e": 1, "l": 3, "o": 2, "W": 1, "r": 1, "d": 1}

result = {}
for i in mystr:
  if i in result.keys():
    result[i] += 1
  else:
    result[i] = 1

print(result)
