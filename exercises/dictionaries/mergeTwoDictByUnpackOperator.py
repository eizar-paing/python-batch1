#Unpacking
def fun(a, b, c, d):
  print(a, b, c, d)

my_list = [1, 2, 3, 4]
fun(*my_list) # 1, 2, 3, 4 => fun(1, 2, 3, 4)

# list1 = [1, 2, 3]
# fun(*list1) # 1, 2, 3 => fun(1, 2, 3)

range(2, 5)
list2 = [2, 5]
range(*list2)

#Packing
def mySum(*args):
  return sum(args)

print(mySum(1, 2, 3, 4, 5)) # (1, 2, 3, 4, 5)
print(mySum(1, 2)) # (1, 2)


#Packing and Unpacking
def getSum(a, b, c):
  return a + b + c

def getUpdate(*args):  #Packing
  args = list(args) # [2, 3, 4]

  args[0] = 1
  args[1] = 2
  # [1, 2, 4]
  result = getSum(*args) #Unpacking
  return result

res = getUpdate(2, 3, 4) # (2, 3, 4) 
print(res)

#For Dictionary
#Unpacking
def fun1(a, b, c):
  print(a, b, c)

d = {"a": 1, "b": 2, "c": 3}
fun1(**d) # 1, 2, 3

#Packing
def fun2(**args): # {"name": }
  for key, value in args.items():
    print(key, " : ", value)

fun2(name="ezp", ID="101", language="Python")

#Merge two Dictionaries
d1 = {"a": 1, "b": 2, "c": 3} # "a": 1, "b": 2, "c": 3
d2 = {"d": 4, "e": 5, "f": 6}
 #{"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

def mergeDict(dict1, dict2):
  result = {**dict1, **dict2}
  return result

merged_result = mergeDict(d1, d2)
print(merged_result)




