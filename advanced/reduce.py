from functools import reduce
num = [1, 2, 3, 4]

def multiply(x):
  return (x*x)

def add(x):
  return (x+x)

result = 0
for i in num:
  result += i

addition = reduce((lambda x, y : x + y), num) # (((1, 2), 3), 4)
print(addition)

multiplication = reduce((lambda x, y: x * y), num)
print(multiplication)



# funcs = [multiply, add]
# for i in num:
#   value = reduce((lambda x, y : y(i)), funcs)
#   print(value)

# for i in num:
#   result = multiply(i)
#   result = add(result)
#   print(result)


num_list = [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]

def mini(a, b):
  # if a < b:
  #   return a
  # else:
  #   return b
  return a if a < b else b

mini_num = reduce(mini, num_list)
print(mini_num)


def maxi(a, b):
  print(a, b)
  return a if a > b else b

maxi_num = reduce(maxi, num_list)
print(maxi_num)
