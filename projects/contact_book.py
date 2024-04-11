contact = {}

# 1. Add new contact
# 2. Search contact
# 3. Display contacts
# 4. Edit contact
# 5. Delete contact
# 6. Exit

def add_contact():
  name = input("Enter the contact name : ")
  phone = input("Enter the contact number : ")
  contact[name] = phone

def search_contact():
  search_name = input("Enter the contact name : ")
  if search_name in contact:
    print(search_name, "'s contact number is ", contact[search_name])
  else:
    print(search_name, "is not found in contact book")

def display_contact():
  if len(contact) > 0:
    print("Name\t\tPhone")
    for key in contact.keys():
      print(key, "\t\t", contact[key])
  else:
    print("No data in contact book")

def edit_contact():
  edit_name = input("Enter the contact name to be edited : ")
  if edit_name in contact:
    phone = input("Enter the contact number : ")
    contact[edit_name] = phone
    print("Contact Updated")
  else:
    print(edit_name, "is not found in contact book")

def delete_contact():
  delete_name = input("Enter the contact name to be deleted : ")
  if delete_name in contact:
    confirmation = input("Are you sure to delete this contact y/n? ")
    if confirmation == 'y' or confirmation == 'Y':
      contact.pop(delete_name)
      print("Contact Deleted")
  else:
    print(delete_name, "is not found in contact book")

while True: 
  choice = int(input("1. Add new contact \n2. Search contact \n3. Display contacts \n4. Edit contact \n5. Delete contact \n6. Exit \nEnter number : "))
  if choice == 1:
    add_contact()
  elif choice == 2:
    search_contact()
  elif choice == 3:
    display_contact()
  elif choice == 4:
    edit_contact()
  elif choice == 5:
    delete_contact()
  else:
    print("Thank you for using the contact book")
    break
