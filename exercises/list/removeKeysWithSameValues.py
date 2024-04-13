#Python program to remove keys with same values in a dictionary.

d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}


# result = {}
# for x,y in d1.items():
#   if y not in result.values():
#     result[x] = y
# print(result)

# ["eleven", 2]
resultList = {}
newList = []
for key, value in d1.items():
  if value in resultList.values():
    newList.append(value)
  else:
    resultList[key] = value

for key, value in list(resultList.items()):
  if value in newList:
    resultList.pop(key)
print(resultList)


vals = list(d1.values())#all values ["eleven", 2, 3, "eleven", 44, 2]
uvals = [v for v in vals if vals.count(v)==1]#unique values
# for v in vals:
#   if vals.count(v) == 1:
#     uvals.append(v)

print(uvals)
d2 = {}
for k,v in d1.items():
   if v in uvals:
      # d2.update({k:v})
      d2[k] = v
print ("dict with unique value:",d2)

tuples = [("one", 1), ("two", 2), ("three", 3)]
result = {"one": 1, "two": 2, "three": 3}

