class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})" 
  
  def new_method(self, num):
  	print("Name ", self.name, " and Age ", self.age, " Num is ", num)
    
def myfun(self):
    print("self ", self)
  

p1 = Person("John", 36)
p2 = Person("Smith", 30)

print(p1)
print(p2)

p1.new_method(5)
p1.myfun()
