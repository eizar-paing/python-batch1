class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
    
  def __str__(self):
    return self.firstname + self.lastname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, email, year):
    super().__init__(fname, lname)
    self.email = email
    self.graduationyear = year
  
  def __str__(self):
    return self.firstname + "/" + self.lastname + "/" + self.email

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

  

x = Student("Mike", "Olsen", "mike@gmail.com", 2019)
x.printname()
print(x)
print(x.email)

y = Student("John", "Smith", "john@gmail.com", 2020)
print(y)
y.welcome()