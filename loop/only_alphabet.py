name = input("Enter user name: ")

size = len(name)

for i in range(size):
  if name[i].isdecimal():
    continue
  print(name[i])