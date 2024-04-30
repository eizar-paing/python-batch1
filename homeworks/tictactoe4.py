from tkinter import *
import tkinter.messagebox as mb

root = Tk()
root.title("Tic Tac Toe")

p1 = StringVar()
p2 = StringVar()
p1_turn = True
flage = 0

def when_click(btn):
    if p1.get() and p2.get():
        global p1_turn, flag

        if btn["text"] == " " and p1_turn:
            btn["text"] = "X"
            p1_turn = False

        elif btn["text"] == " " and not p1_turn:
            btn["text"] = "O"
            p1_turn = True
        
        else:
            mb.showinfo("Tic Tac Toe 4", "Already Filled!")
    else:
        mb.showinfo("Tic Tac Toe 4", "Enter names first")

def check_winner():
    if(button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X" and button_4["text"] == "X" or
    button_5["text"] == "X" and button_6["text"] == "X" and button_7["text"] == "X" and button_8["text"] == "X" or
    button_9["text"] == "X" and button_10["text"] == "X" and button_11["text"] == "X" and button_12["text"] == "X" or
    button_13["text"] == "X" and button_14["text"] == "X" and button_15["text"] == "X" and button_16["text"] == "X" or
    button_1["text"] == "X" and button_6["text"] == "X" and button_11["text"] == "X" and button_16["text"] == "X" or
    button_4["text"] == "X" and button_7["text"] == "X" and button_10["text"] == "X" and button_13["text"] == "X" or
    button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X" and button_13["text"] == "X" or
    button_2["text"] == "X" and button_6["text"] == "X" and button_10["text"] == "X" and button_14["text"] == "X" or
    button_3["text"] == "X" and button_7["text"] == "X" and button_11["text"] == "X" and button_15["text"] == "X" or
    button_4["text"] == "X" and button_8["text"] == "X" and button_12["text"] == "X" and button_16["text"] == "X" or):
        mb.showinfo("Tic Tac Toe 4", p1.get() + "wins")
    
    elif(button_1["text"] == "X" and button_2["text"] == "X" and button_3["text"] == "X" and button_4["text"] == "X" or
    button_5["text"] == "X" and button_6["text"] == "X" and button_7["text"] == "X" and button_8["text"] == "X" or
    button_9["text"] == "X" and button_10["text"] == "X" and button_11["text"] == "X" and button_12["text"] == "X" or
    button_13["text"] == "X" and button_14["text"] == "X" and button_15["text"] == "X" and button_16["text"] == "X" or
    button_1["text"] == "X" and button_6["text"] == "X" and button_11["text"] == "X" and button_16["text"] == "X" or
    button_4["text"] == "X" and button_7["text"] == "X" and button_10["text"] == "X" and button_13["text"] == "X" or
    button_1["text"] == "X" and button_5["text"] == "X" and button_9["text"] == "X" and button_13["text"] == "X" or
    button_2["text"] == "X" and button_6["text"] == "X" and button_10["text"] == "X" and button_14["text"] == "X" or
    button_3["text"] == "X" and button_7["text"] == "X" and button_11["text"] == "X" and button_15["text"] == "X" or
    button_4["text"] == "X" and button_8["text"] == "X" and button_12["text"] == "X" and button_16["text"] == "X" or):
        mb.showinfo("Tic Tac Toe 4", p2.get() + "wins")
    

def restart_button():
    global p1_turn, flage
    p1.set(" ")
    p2.set(" ")
    p1_turn = True
    flag = 0
    button_1["text"] =  button_2["text"] =  button_3["text"] =  button_4["text"] =  button_5["text"] =  button_6["text"] =  button_7["text"] =  button_8["text"] =  button_9["text"] =  button_10["text"] =  button_11["text"] =  button_12["text"] =  button_13["text"] =  button_14["text"] =  button_15["text"] =  button_16["text"] = " "
    button_1.config(state=NORMAL)
    button_2.config(state=NORMAL)
    button_3.config(state=NORMAL)
    button_4.config(state=NORMAL)
    button_5.config(state=NORMAL)
    button_6.config(state=NORMAL)
    button_7.config(state=NORMAL)
    button_8.config(state=NORMAL)
    button_9.config(state=NORMAL)
    button_10.config(state=NORMAL)
    button_11.config(state=NORMAL)
    button_12.config(state=NORMAL)
    button_13.config(state=NORMAL)
    button_14.config(state=NORMAL)
    button_15.config(state=NORMAL)
    button_16.config(state=NORMAL)




label_1 = Label(root, text="Player1", bg="grey", fg="black")
label_1.grid(row=0, column=0)
player1 = Entry(root, textvariable=p1, width=10, bd=2)
player1.grid(row=0, column=1)

label_2 = Label(root, text="Player2", bg="grey", fg="black")
label_2.grid(row=1, column=0)
player2 = Entry(root, textvariable=p2, width=10, bd=2)
player2.grid(row=1, column=1)

restart = Button(root, text='Restart', fg='black', command= lambda : restart_button())
restart.grid(row=1, column=2)

button_1 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_1))
button_1.grid(row=2, column=0)

button_2 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_2))
button_2.grid(row=2, column=1)

button_3 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_3))
button_3.grid(row=2, column=2)

button_4 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_4))
button_4.grid(row=2, column=3)

###
button_5 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_5))
button_5.grid(row=3, column=0)

button_6 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_6))
button_6.grid(row=3, column=1)

button_7 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_7))
button_7.grid(row=3, column=2)

button_8 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_8))
button_8.grid(row=3, column=3)


###
button_9 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_9))
button_9.grid(row=4, column=0)

button_10 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_10))
button_10.grid(row=4, column=1)

button_11 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_11))
button_11.grid(row=4, column=2)

button_12= Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_12))
button_12.grid(row=4, column=3)

###
button_13 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_13))
button_13.grid(row=5, column=0)

button_14 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_14))
button_14.grid(row=5, column=1)

button_15 = Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_15))
button_15.grid(row=5, column=2)

button_16= Button(root, text=" ", fg="black", width=8, height=4, command=lambda: when_click(button_16))
button_16.grid(row=5, column=3)

root.mainloop()