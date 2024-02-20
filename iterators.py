# create iterator for string
my_str = "hello!"
for i in my_str:
  print(i)

myit = iter(my_str)
print(next(myit))
print(next(myit))

# create iterator for tuple
mytuple = ("apple", "banana", "cherry")
mytuple_it = iter(mytuple)

print(next(mytuple_it))
print(next(mytuple_it))


class MyNumbers: #class
  def __init__(self) -> None:
    print("do init function !!!")

  def __iter__(self):
    self.a = 1
    return self
  
  def __next__(self):
    print("next call!")
    if self.a <= 10:
      x = self.a  #1 #2 # 3
      self.a += 1 #2 #3 # 4
      return x
    else:
      raise StopIteration


mynum = MyNumbers() #object
mynum_it = iter(mynum) # (1)

for i in mynum_it:
  print(i)
print("end of for loop")

# print(next(mynum_it)) # 1
# print(next(mynum_it)) # 2
# print(next(mynum_it)) # 3
# print(next(mynum_it)) # 4
# print(next(mynum_it)) # 5
# print(next(mynum_it)) # 6
# print(next(mynum_it)) # 7
# print(next(mynum_it)) # 8
# print(next(mynum_it)) # 9
# print(next(mynum_it)) # 10
# print(next(mynum_it)) # 11 // error occurs

print("*************")
num_list = [1, 2, 3, 4, 5]
mylist_it = iter(num_list)
print(next(mylist_it))
print(next(mylist_it)) 
print(next(mylist_it))
print(next(mylist_it)) 
print(next(mylist_it))