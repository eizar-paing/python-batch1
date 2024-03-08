import turtle

def draw_star(size, color):
  turtle.fillcolor(color)
  turtle.begin_fill()
  for i in range(5):
    turtle.forward(size)
    turtle.right(144)
  turtle.end_fill()

def call_star(size, color, x, y):
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  draw_star(size, color)

call_star(100, 'red', 0, 0)
call_star(80, 'green', 0, 120)
call_star(50, 'yellow', 100, 120)

turtle.done()