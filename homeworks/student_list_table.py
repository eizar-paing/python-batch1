from tkinter import *

student_list = [] # []

def save_btn():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())
    student_info = "name", name, "mark1", mark1, "mark2", mark2, "mark3", mark3
    student_list.append(student_info)

def list_to_dict(std_list):
    new_res = {}
    for i in std_list:
        pass
        
huhu = list_to_dict(student_list)





root = Tk()
root.title("Student Tabel")
root.geometry("500x500")
root.configure(background="grey")

label_1 = Label(root, text= "Name", bg= "white", fg="black", width=8, font="15").place(x= 50, y = 50)
label_2 = Label(root, text= "Mark1", bg= "white", fg="black", width=8, font="15").place(x= 50, y = 130)
label_3 = Label(root, text= "Mark2", bg= "white", fg="black", width=8, font="15").place(x= 50, y = 210)
label_4 = Label(root, text= "Mark3", bg= "white", fg="black", width=8, font="15").place(x= 50, y = 290)

name_entry = Entry(root, width=30)
name_entry.place(x=200, y = 50)
mark1_entry = Entry(root, width=30)
mark1_entry.place(x=200, y = 130)
mark2_entry = Entry(root, width=30)
mark2_entry.place(x=200, y = 210)
mark3_entry = Entry(root, width=30)
mark3_entry.place(x=200, y = 290)

save = Button(root, text="Save", font="15", bg="white", fg="black", width=8, command= lambda : save_btn()).place(x=150, y=370)


root.mainloop()

print(student_list)
