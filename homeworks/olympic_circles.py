import turtle

screen = turtle.Screen()
screen.bgcolor("white")
# screen.setup(800, 800)

mypen = turtle.Turtle()
mypen.pensize(18)
mypen.shape("turtle")


def draw_circle(color, x, y):
    mypen.pencolor(color)
    mypen.penup()
    mypen.goto(x, y)
    mypen.pendown()
    mypen.circle(100)

mypen.hideturtle()

draw_circle("blue", -250, 10)
draw_circle("black", 0, 10)
draw_circle("red", 250, 10)
draw_circle("yellow", -125, -70)
draw_circle("green", 125, -70)

screen.mainloop()