name = ["Jame", "John", "Rose", "Mary"]

def search_name(nameString):
  i = 0
  res = False
  while i < len(name):
    if name[i] == nameString:
      res = True
      break
    else:
      res = False
    i += 1
  return res

result = False
while not(result):
  user_name = input("Enter user name: ")
  result = search_name(user_name)
print("There is user name!")


# i = 0 => "Jame" == "John", res = False
# i = 1 => "John" == "John", res = True
# i = 2 => "Rose" == "John", res = False
# i = 3 => "Mary" == "John", res = False
