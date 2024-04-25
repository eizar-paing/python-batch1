from tkinter import *

class Table:
  def __init__(self, root):
    for i in range(total_rows): #　0 to 4
      for j in range(total_cols): # 0 to 3
        self.entry = Entry(root, width=20)
        self.entry.grid(row=i, column=j)
        self.entry.insert(0, list[i][j])

    # i = 0 => j = 0 to 3 => list[i][j]
                          #=> list[0][0]
                          #=> list[0][1]
                          #=> list[0][2]
                          #=> list[0][3]

    # i = 1 => j = 0 to 3 => list[i][j]
                          #=> list[1][0]
                          #=> list[1][1]
                          #=> list[1][2]
                          #=> list[1][3]

student_data = [{'id': 1, 'name': "Student 1", "mark1": 40, "mark2": 70, "mark3": 70 },
{'id': 2, 'name': "Student 2", "mark1": 40, "mark2": 70, "mark3": 70 },
{'id': 1, 'name': "Student 3", "mark1": 40, "mark2": 70, "mark3": 70 }]

list = [(1,'Raj','Mumbai',19),
       (2,'Aaryan','Pune',18),
       (3,'Vaishnavi','Mumbai',20),
       (4,'Rachna','Mumbai',21),
       (5,'Shubham','Delhi',21)]

total_rows = len(list)
total_cols = len(list[0])

root = Tk()
Table(root)
root.mainloop()