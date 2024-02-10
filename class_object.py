class Student:
  twitter = "@kyaw kyaw"
  def __init__(self, name, email, address, phone):
    self.phone = phone
    self.name = name
    self.email = email
    self.address = address
    

kyawkyaw = Student("Kyaw Kyaw", "kyaw@eg.com", "address one", "123 444 666")
mgmg = Student("Mg Mg", "mgmg@eg.com", "address two", "222 444 888")

print(kyawkyaw.phone)
print(mgmg.twitter)