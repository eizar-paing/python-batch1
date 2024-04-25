student_list = []

class Student:
  def __init__(other, name, mark1, mark2, mark3):
    # other.student_id = len(student_list) + 1
    other.student_id = student_list[len(student_list)-1].id + 1
    other.name = name
    other.mark1 = mark1
    other.mark2 = mark2
    other.mark3 = mark3
    
  def __str__(self) -> str:
    return f"{self.name}, {self.mark1}, {self.mark2}, {self.mark3} and id {self.student_id}."

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
    id = int(input("Enter the student id : "))
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

# Susan
def edit_student():
  if len(student_list) > 0:
    user_id = int(input("Enter the student id: ")) # 1
    for student in student_list: #1, 2, 3
      if student.student_id == user_id:
        attribute = input("Enter the attribute name to edit (name, mark1, mark2, mark3) : ")
        value = input("Enter the new value : ")
        setattr(student, attribute, value)
        print("Upadated new student successfully!")
        break
      else:
          print("No student with id ", user_id)
  else:
    print("No students in the list")
# Susan

# def edit_student():
#   if len(student_list) > 0:
#     id = input("Enter the student id : ")
#     attribute = input("Enter the attribute name to edit (name, mark1, mark2, mark3) : ")
#     value = input("Enter the new value : ")
#     #To trace
#     for student in student_list:
#       if student.student_id == id:
#         setattr(student, attribute, value)
#         print("Upadated new student successfully!")
#       else:
#         print("No student with id ", id)
#   else:
#     print("No student in student list!")

def delete_student():
  id = int(input("Enter the student id : "))
  for student in student_list:
    if student.student_id == id:
      confirmation = input("Are you sure to delete this student y/n? ")
      if confirmation == 'y' or confirmation == 'Y':
        student_list.remove(student)
        print("Deleted student successfully!")
        break
    else:
      print("No student to be deleted!")

def calculate_grade(student):
  total = int(student.mark1) + int(student.mark2) + int(student.mark3)
  average_mark = total/3
  if average_mark > 90 and average_mark <= 100:
      print("Grade of the student is A1")
  elif average_mark > 80 and average_mark <= 90:
      print("Grade of the student is A2")
  elif average_mark > 70 and average_mark <= 80:
      print("Grade of the student is B1")
  elif average_mark > 60 and average_mark <= 70:
      print("Grade of the student is B2")
  elif average_mark > 50 and average_mark <= 60:
      print("Grade of the student is C1")
  elif average_mark > 40 and average_mark <= 50:
      print("Grade of the student is C2")
  elif average_mark > 32 and average_mark <= 40:
      print("Grade of the student is D")
  elif average_mark > 20 and average_mark <= 32:
      print("Grade of the student is E1")
  else:
      print("Grade of the student is E2")

def view_grade():
  if len(student_list) > 0:
    id = int(input("Enter the student id : "))
    for student in student_list:
      if student.student_id == id:
        calculate_grade(student)
        break
      else:
        print("No student to view grade!")
  else:
    print("No students in the list")

while True:
  choice = int(input("1. Add new student \n2. Search student \n3. Display students \n4. Edit student \n5. Delete student \n6. View Grade  \n7. Exit \nEnter number : "))
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
  elif choice == 6:
    view_grade()
  else:
    print("Thank you for using the student list")
    break


# student = Student("susan", 100, 92, 78)
# print(student)

# student1 = Student("BoBo", 100, 92, 78)
# print(student1)