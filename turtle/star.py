import turtle

w = turtle.Screen()
w.bgcolor('green')

t = turtle.Turtle()
t.pencolor('red')
t.pensize(3)
t.fillcolor('black')
t.begin_fill()
t.circle(108)
t.end_fill()

t.circle(-100, 90)
t.forward(100)
# t.fillcolor('blue')
# t.color('red')
# t.fillcolor('yellow')
# t.begin_fill()
# for i in range(5):
#   t.forward(200)
#   t.right(144)
# t.end_fill()
# t.right(108)
turtle.done()
