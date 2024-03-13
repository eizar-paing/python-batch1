import turtle

w = turtle.Screen()
w.bgcolor('green')
w.setup(800, 800)
t = turtle.Turtle()

def draw_polygon(sides, length):
  angle = 360/sides
  for i in range(0, sides):
    t.forward(length)
    t.left(angle)

draw_polygon(3, 150)
t.penup()
t.goto(100, 100)
t.pendown()
draw_polygon(4, 150)
t.hideturtle()
turtle.done()
