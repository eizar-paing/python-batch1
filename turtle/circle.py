import turtle

w = turtle.Screen()
w.bgcolor('green')

t = turtle.Turtle()
colors = ['blue', 'gray', 'red', 'yellow']

t.fillcolor('blue')
t.begin_fill()
t.circle(100, 90)
t.lt(90)
t.fd(100)
t.goto(0, 0)
t.end_fill()
t.lt(180)
t.circle(100, 90)

t.fillcolor('red')
t.begin_fill()
t.circle(100, 90)
t.lt(90)
t.fd(100)
t.goto(0, 100)
t.end_fill()
t.bk(100)
t.rt(90)


# for i in range(4):
#   t.fillcolor(colors[i])
#   t.begin_fill()
#   t.circle(100, 90)
#   t.lt(90)
#   t.fd(100)
#   t.bk(100)
#   t.right(90)
#   t.end_fill()

turtle.done()