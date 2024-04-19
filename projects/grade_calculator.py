from tkinter import *

def calculate():
  english = int(english_entry.get())
  math = int(math_entry.get())
  science = int(science_entry.get())
  total = english + math + science
  totalvalue.config(text=total)
  average = int(total/3)
  averagevalue.config(text=average)
  if average > 50:
    result = "PASS"
    color = "blue"
  else:
    result = "FAIL"
    color = "red"
  resultvalue.config(text=result, fg=color)
  
root = Tk()
root.title("Grade Calculator")
root.geometry("500x400")
root.configure(background="white")

Label(root, text="English", font="15", fg="black", bg="white").place(x=50,y=20)
Label(root, text="Math", font="15", fg="black", bg="white").place(x=50,y=70)
Label(root, text="Science", font="15", fg="black", bg="white").place(x=50,y=120)
Label(root, text="Total", font="15", fg="black", bg="white").place(x=50,y=170)
Label(root, text="Average", font="15", fg="black", bg="white").place(x=50,y=220)
Label(root, text="Result", font="15", fg="black", bg="white").place(x=50,y=270)

english_entry = Entry(root, width=20)
english_entry.place(x=200, y=20)
math_entry = Entry(root, width=20)
math_entry.place(x=200, y=70)
science_entry = Entry(root, width=20)
science_entry.place(x=200, y=120)

totalvalue = Label(root, text="", font="15", fg="black", bg="white")
totalvalue.place(x=200, y=170)
averagevalue = Label(root, text="", font="15", fg="black", bg="white")
averagevalue.place(x=200, y=220)
resultvalue = Label(root, text="", font="bold 15", fg="black", bg="white")
resultvalue.place(x=200, y=270)

Button(root, text="Calculate", bd=2, command=lambda : calculate()).place(x=50, y=320)
Button(root, text="Exit", bd=2, command=lambda : exit()).place(x=200, y=320)

root.mainloop()