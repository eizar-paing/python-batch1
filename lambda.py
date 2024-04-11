def add(a, b):
  return a + b
result = add(1, 2)
print(result)

add2 = lambda a, b: a + b
result2 = add2(2, 2)
print(result2)

# Not OK
def first(a):
  def second(b):
    print(b)
    return a + b
  second(4)
print(first(10))


# Power of Lambda function
def function1(a):
  return lambda b : a + b

lamb_fun = function1(10) # lambda b : 10 + b

print(lamb_fun(2))

# eg of double and trouble
def double(n):
  return n * 2
def triple(n):
  return n * 3

def myfunction(n, a):
  return n * a

print(double(10))
print(triple(10))
print(myfunction(10, 2))
print(myfunction(10, 3))

# Lambda function of double and trouble
def myfun_lamb(n):
  return lambda a : n * a
double_fun = myfun_lamb(2) # lambda a : 10 * a
triple_fun = myfun_lamb(3)

print(double_fun(10))
print(triple_fun(10))


# 
def double(a):
  return a * 2

def multi10(a):
  return a * 10

def add2(a):
  return a + 2

result = multi10(add2(double(10)))

func = double(5) # 10

func = lambda x : double(x) #double(5)
print("lambda result 1 : ", func(3))

result = lambda x : x + 1
print("lambda result 2 : ", result(3))
