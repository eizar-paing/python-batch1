import turtle

w = turtle.Screen()
w.bgcolor('green')

t = turtle.Turtle()
t.pencolor('red')
t.pensize(3)

t.fillcolor('blue')
t.begin_fill()
for i in range(5):
  t.forward(200)
  t.right(144)
t.end_fill()
t.right(90)
t.circle(100)
turtle.done()
