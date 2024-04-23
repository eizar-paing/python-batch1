from tkinter import *
import tkinter.messagebox as mb

root = Tk()
root.title("Tic Tac Toe")

p1 = StringVar()
p2 = StringVar()
p1_turn = True
flag = 0

def btn_click(btn):
  global p1_turn, flag
  if btn['text'] =='' and p1_turn:
    btn['text'] = 'X'
    p1_turn = False
    checkwinner()
  elif btn['text'] == '' and not p1_turn:
    btn['text'] ='O'
    p1_turn = True
    checkwinner()
  else:
    mb.showinfo("Tic Tac Toe", "Already filled!")

def checkwinner():
  if(btn1['text'] == 'X' and btn2['text'] == 'X' and btn3['text'] == 'X' or
  btn4['text'] == 'X' and btn5['text'] == 'X' and btn6['text'] == 'X' or
  btn7['text'] == 'X' and btn8['text'] == 'X' and btn9['text'] == 'X' or
  btn1['text'] == 'X' and btn4['text'] == 'X' and btn7['text'] == 'X' or
  btn2['text'] == 'X' and btn5['text'] == 'X' and btn8['text'] == 'X' or
  btn3['text'] == 'X' and btn6['text'] == 'X' and btn9['text'] == 'X' or
  btn1['text'] == 'X' and btn5['text'] == 'X' and btn9['text'] == 'X' or
  btn3['text'] == 'X' and btn5['text'] == 'X' and btn7['text'] == 'X'):
    mb.showinfo("Tic Tac Toe", p1.get() + " wins!")
    disabled_btn()
    # player1 win
  elif(btn1['text'] == 'O' and btn2['text'] == 'O' and btn3['text'] == 'O' or
  btn4['text'] == 'O' and btn5['text'] == 'O' and btn6['text'] == 'O' or
  btn7['text'] == 'O' and btn8['text'] == 'O' and btn9['text'] == 'O' or
  btn1['text'] == 'O' and btn4['text'] == 'O' and btn7['text'] == 'O' or
  btn2['text'] == 'O' and btn5['text'] == 'O' and btn8['text'] == 'O' or
  btn3['text'] == 'O' and btn6['text'] == 'O' and btn9['text'] == 'O' or
  btn1['text'] == 'O' and btn5['text'] == 'O' and btn9['text'] == 'O' or
  btn3['text'] == 'O' and btn5['text'] == 'O' and btn7['text'] == 'O'):
    mb.showinfo("Tic Tac Toe", p2.get() + " wins!")
    disabled_btn()
    
def disabled_btn():
  btn1.config(state=DISABLED)
  btn2.config(state=DISABLED)
  btn3.config(state=DISABLED)
  btn4.config(state=DISABLED)
  btn5.config(state=DISABLED)
  btn6.config(state=DISABLED)
  btn7.config(state=DISABLED)
  btn8.config(state=DISABLED)
  btn9.config(state=DISABLED)

def restart_btn():
  global p1_turn, flag
  p1.set('')
  p2.set('')
  p1_turn = True
  flag = 0
  btn1['text'] = btn2['text'] = btn3['text'] = btn4['text'] = btn5['text'] = btn6['text'] = btn7['text'] = btn8['text'] = btn9['text'] = ''
  btn1.config(state=NORMAL)
  btn2.config(state=NORMAL)
  btn3.config(state=NORMAL)
  btn4.config(state=NORMAL)
  btn5.config(state=NORMAL)
  btn6.config(state=NORMAL)
  btn7.config(state=NORMAL)
  btn8.config(state=NORMAL)
  btn9.config(state=NORMAL)



label1 = Label(root, text='Player1', bg='white', fg='black')
label1.grid(row=0, column=0)
player1 = Entry(root, textvariable=p1, width=10, bd=2)
player1.grid(row=0, column=1)

label2 = Label(root, text='Player2', bg='white', fg='black')
label2.grid(row=1, column=0)
player2 = Entry(root, textvariable=p2, width=10, bd=2)
player2.grid(row=1, column=1)

restart = Button(root, text='Restart', fg='black', command=lambda : restart_btn())
restart.grid(row=1, column=2)

btn1 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn1))
btn1.grid(row=2, column=0)
btn2 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn2))
btn2.grid(row=2, column=1)
btn3 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn3))
btn3.grid(row=2, column=2)

btn4 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn4))
btn4.grid(row=3, column=0)
btn5 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn5))
btn5.grid(row=3, column=1)
btn6 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn6))
btn6.grid(row=3, column=2)

btn7 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn7))
btn7.grid(row=4, column=0)
btn8 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn8))
btn8.grid(row=4, column=1)
btn9 = Button(root, text='', fg='black', width=8, height=4, command= lambda : btn_click(btn9))
btn9.grid(row=4, column=2)

root.mainloop()