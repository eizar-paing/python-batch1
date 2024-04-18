student_list = []

class Student:
  def __init__(other, name, mark1, mark2, mark3):
    other.student_id = len(student_list) + 1
    other.name = name
    other.mark1 = mark1
    other.mark2 = mark2
    other.mark3 = mark3
    
  def __str__(self) -> str:
    return f"My name is {self.name} and My email is {self.email}."

def add_student():
  name = input("Enter the student name : ")
  mark1 = input("Enter the student mark1 : ")
  mark2 = input("Enter the student mark2 : ")
  mark3 = input("Enter the student mark3 : ")
  student = Student(name, mark1, mark2, mark3)
  student_list.append(student)
  print("Added new student successfully!")

def search_student():
  if len(student_list) > 0:
    id = input("Enter the student id : ")
    for student in student_list:
      if student.student_id == id:
        print("ID : ", student.student_id, ", Name : ", student.name, ", Mark1 : ", student.mark1, ", Mark2 : ", student.mark2, ", Mark3 : ", student.mark3)
      else:
        print(id, "is not found in studnet list")
  else:
    print("No student in student list!")

def display_student():
  if len(student_list) > 0:
    for student in student_list:
      print("ID : ", student.student_id, ", Name : ", student.name, ", Mark1 : ", student.mark1, ", Mark2 : ", student.mark2, ", Mark3 : ", student.mark3)
  else:
    print("No student in student list!")

def edit_student():
  if len(student_list) > 0:
    id = input("Enter the student id : ")
    attribute = input("Enter the attribute name to edit (name, mark1, mark2, mark3) : ")
    value = input("Enter the new value : ")
    #To trace
    for student in student_list:
      if student.student_id == id:
        setattr(student, attribute, value)
        print("Upadated new student successfully!")
      else:
        print("No student with id ", id)
  else:
    print("No student in student list!")

def delete_student():
  id = input("Enter the student id : ")
  for student in student_list:
    if student.student_id == id:
      student_list.remove(student)
      print("Deleted student successfully!")

while True:
  choice = int(input("1. Add new student \n2. Search student \n3. Display students \n4. Edit student \n5. Delete student \n6. Exit \nEnter number : "))
  if choice == 1:
    add_student()
  elif choice == 2:
    search_student()
  elif choice == 3:
    display_student()
  elif choice == 4:
    edit_student()
  elif choice == 5:
    delete_student()
  else:
    print("Thank you for using the student list")
    break