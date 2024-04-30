items = [1, 2, 3, 4, 5] 
squares = []
for i in items:
  sq = i**2
  squares.append(sq)

print(squares)

map_squares = list(map(lambda x: x**2 , items))
print(map_squares)

# => ['odd', 'even', 'odd', 'even', 'odd']
def checkEvenOdd(num):
  if(num%2==0):
    return 'even'
  else:
    return 'odd'

even_odd_list = list(map(checkEvenOdd, items))
print(even_odd_list)


def multiply(x):
  return (x*x)

def add(x):
  return (x+x)

funs = [multiply, add]
for i in range(5):
  value = list(map(lambda x: x(i), funs)) # [multiply(0),add(0)] => [0, 0]
  print(value)


# [0, 1, 2, 3, 4] => [0, 0]
                # => [1, 2]
                # => [4, 4]




