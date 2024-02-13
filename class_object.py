class Student:
  twitter = "@kyaw kyaw"
  def __init__(other, name, email, address, phone, mark1, mark2, mark3):
    other.phno = phone
    other.name = name
    other.email = email
    other.address = address
    other.mark1 = mark1
    other.mark2 = mark2
    other.mark3 = mark3
    
  def __str__(self) -> str:
    return f"My name is {self.name} and My email is {self.email}."
  
  def capName(self):
    print("I am ", self.name.capitalize())
  
  def getResult(self):
    if(self.mark1 >=40 and self.mark2 >= 40 and self.mark3 >= 40):
      print(self.name , "is passed.")
    else:
      print(self.name , "is failed.")

  
student1 = Student("Kyaw Kyaw", "kyaw@eg.com", "address one", "123 444 666", 30, 50, 60)
student2 = Student("Mg Mg", "mgmg@eg.com", "address two", "222 444 888", 50, 60, 70)

print(student1.phno)
print(student2.twitter)

print(student1)

student1.capName()
student1.getResult()
student2.getResult()