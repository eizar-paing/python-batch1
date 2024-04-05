from tkinter import *

def getDigit(digit):
  current = result_label['text']
  new = current + str(digit)
  result_label.config(text=new)

def clear():
  result_label.config(text='')

def removeDigit():
  current = int(result_label['text'])
  new = int(current / 10)
  if new == 0:
    result_label.config(text='')
  else:
    result_label.config(text=new)

def getOperator(op):
  global number1, operator
  number1 = int(result_label['text'])
  operator = op
  result_label.config(text='')

def getResult():
  number2 = int(result_label['text'])
  if operator == '+':
    result = number1 + number2
  elif operator == '-':
    result = number1 - number2
  elif operator == '*':
    result = number1 * number2
  else:
    if number2 == 0:
      result = 'Error'
    else:
      result = number1 / number2
  result_label.config(text=str(result))

root = Tk()
root.title("Calculator")
root.geometry('500x400')
root.resizable(1, 0)
root.configure(background='black')

result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=4, pady=(40, 20))
result_label.config(font=('Verdana', 32, 'bold'))

# command = getDigit(7)  #None
# command = lambda : getDigit(7) #getDigit(7)

btn7 = Button(root, text='7', width=5, height=2, command= getDigit(7))
btn7.grid(row=1, column=0)
btn7.config(font=('Verdana', 14))

btn8 = Button(root, text='8', width=5, height=2, command= lambda :getDigit(8))
btn8.grid(row=1, column=1)
btn8.config(font=('Verdana', 14))

btn9 = Button(root, text='9', width=5, height=2, command=lambda :getDigit(9))
btn9.grid(row=1, column=2)
btn9.config(font=('Verdana', 14))

btn_add = Button(root, text='+', width=5, height=2, command=lambda :getOperator('+'))
btn_add.grid(row=1, column=3)
btn_add.config(font=('Verdana', 14))

btn4 = Button(root, text='4', width=5, height=2, command=lambda :getDigit(4))
btn4.grid(row=2, column=0)
btn4.config(font=('Verdana', 14))

btn5 = Button(root, text='5', width=5, height=2, command=lambda :getDigit(5))
btn5.grid(row=2, column=1)
btn5.config(font=('Verdana', 14))

btn6 = Button(root, text='6', width=5, height=2, command=lambda :getDigit(6))
btn6.grid(row=2, column=2)
btn6.config(font=('Verdana', 14))

btn_sub = Button(root, text='-', width=5, height=2, command=lambda :getOperator('-'))
btn_sub.grid(row=2, column=3)
btn_sub.config(font=('Verdana', 14))


btn1 = Button(root, text='1', width=5, height=2, command=lambda :getDigit(1))
btn1.grid(row=3, column=0)
btn1.config(font=('Verdana', 14))

btn2 = Button(root, text='2', width=5, height=2, command=lambda :getDigit(2))
btn2.grid(row=3, column=1)
btn2.config(font=('Verdana', 14))

btn3 = Button(root, text='3', width=5, height=2, command=lambda :getDigit(3))
btn3.grid(row=3, column=2)
btn3.config(font=('Verdana', 14))

btn_mul = Button(root, text='*', width=5, height=2, command=lambda :getOperator('*'))
btn_mul.grid(row=3, column=3)
btn_mul.config(font=('Verdana', 14))

btn0 = Button(root, text='0', width=5, height=2, command=lambda :getDigit(0))
btn0.grid(row=4, column=0)
btn0.config(font=('Verdana', 14))

btn_clear = Button(root, text='C', width=5, height=2, command=lambda :clear())
btn_clear.grid(row=4, column=1)
btn_clear.config(font=('Verdana', 14))

btn_equal = Button(root, text='=', width=5, height=2, command=lambda :getResult())
btn_equal.grid(row=4, column=2)
btn_equal.config(font=('Verdana', 14))

btn_div = Button(root, text='/', width=5, height=2, command=lambda :getOperator('/'))
btn_div.grid(row=4, column=3)
btn_div.config(font=('Verdana', 14))

btn_remove = Button(root, text='AC', width=5, height=2, command=lambda :removeDigit())
btn_remove.grid(row=5, column=1)
btn_remove.config(font=('Verdana', 14))

root.mainloop()
