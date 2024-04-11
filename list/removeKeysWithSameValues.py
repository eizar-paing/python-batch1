d1 = {"one":"eleven", "2":2, "three":3, "11":"eleven", "four":44, "two":2}


result = {}
for x,y in d1.items():
  if y not in result.values():
    result[x] = y
print(result)