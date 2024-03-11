import turtle

w = turtle.Screen()
w.bgcolor('white')

t = turtle.Turtle()
t.pensize(2)

t.fillcolor('blue')
t.begin_fill()
t.circle(100, 90)
t.lt(90)
t.fd(100)
t.goto(0, 0)
t.end_fill()
t.lt(180) # diff - red, yellow
t.circle(100, 90) # diff - red, yellow


t.fillcolor('red')
t.begin_fill()
t.circle(100, 90)
t.lt(90)
t.goto(0, 100)
t.end_fill()
t.bk(100) # diff - blue, purple/ same - yellow
t.rt(90) # diff - blue, purple/ same - yellow

t.fillcolor("yellow")
t.begin_fill()
t.circle(100, 90)
t.lt(90)
t.goto(0, 100)
t.end_fill()
t.bk(100) # diff - blue, purple/ same - red
t.rt(90) # diff - blue, purple/ same - red

t.fillcolor('purple')
t.begin_fill()
t.circle(100, 90)
t.lt(90)
t.goto(0, 100)
t.end_fill()
# t.bk(100)

# diff - blue, red, yellow
# diff - blue, red, yellow

# def draw_90_circle(color, x, y):
#     t.fillcolor(color)
#     t.begin_fill()
#     t.circle(100, 90)
#     t.lt(90)
#     t.fd(100)
#     t.goto(x, y)
#     t.end_fill()
#     t.lt(180)
#     t.circle(100 , 90)

# draw_90_circle("light green", 0, 0)
# draw_90_circle("light blue", 0, 100)
# draw_90_circle("purple", 0, 100)
# draw_90_circle("light pink", 0, 100)

turtle.done()