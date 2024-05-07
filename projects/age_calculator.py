from tkinter import *
from datetime import date

root = Tk()
root.title("Age Calculator")
root.configure(bg='white')

def calculate_age():
  dob = dateEntry.get()
  # print("dob entry ", dob)
  # print(type(dob))
  dob_date = date.fromisoformat(dob) # 1991-10-06
  # print("dob date ", dob_date)
  # print(type(dob_date))
  current_date = date.today()
  age = current_date - dob_date # end_date - start_date
  print(age)
  print(type(age))
  years = age.days // 365

  displayLabel.config(text=f"You are {years} years old.")

label1 = Label(root, text='Enter your date of birth (YYYY-MM-DD): ', bg='white', fg='black')
label1.grid(row=0, column=0)

dateEntry = Entry(root, width=20, bd=2)
dateEntry.grid(row=1, column=0)

calculateButton = Button(root, text='Calculate Age', bg='black', command= lambda: calculate_age())
calculateButton.grid(row=2, column=0)

displayLabel = Label(root, text='', bg='white', fg='black')
displayLabel.grid(row=3, column=0)

root.mainloop()