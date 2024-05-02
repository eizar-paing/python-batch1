from tkinter import *
import csv

root = Tk()

def getStudent():
  csvfile = open('student.csv', "r")
  reader = csv.reader(csvfile)
  row_no = 5
  for row in reader:
    entry = Entry(root, width=20)
    entry.grid(row=row_no, column=0)
    entry.insert(0, row[0])
    entry = Entry(root, width=20)
    entry.grid(row=row_no, column=1)
    entry.insert(0, row[1])
    entry = Entry(root, width=20)
    entry.grid(row=row_no, column=2)
    entry.insert(0, row[2])
    row_no += 1
    print(row[0], ' : ', row[1], ' : ', row[2])

def saveStudent():
  studentName = studentEntry.get()
  className = classEntry.get()
  mark = markEntry.get()

  csv_file = open("student.csv", "a")
  csv_writer = csv.writer(csv_file)
  csv_writer.writerow([studentName, className, mark])

  studentEntry.delete(0, END)
  classEntry.delete(0, END)
  markEntry.delete(0, END)
  

label1 = Label(root, text='Student Name:')
label1.grid(row=0, column=0)
studentEntry = Entry(root, width=20, bd=2)
studentEntry.grid(row=0, column=1, columnspan=2)

label2 = Label(root, text='Class:')
label2.grid(row=1, column=0)
classEntry = Entry(root, width=20, bd=2)
classEntry.grid(row=1, column=1, columnspan=2)

label3 = Label(root, text='Mark:')
label3.grid(row=2, column=0)
markEntry = Entry(root, width=20, bd=2)
markEntry.grid(row=2, column=1, columnspan=2)

saveButton = Button(root, text="Save", command=lambda : saveStudent())
saveButton.grid(row=3, column=1)

label4 = Label(root, text='Student Data')
label4.grid(row=4, column=0)

getStudent()
root.mainloop()