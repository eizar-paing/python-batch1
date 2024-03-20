import turtle

screen = turtle.Screen()
screen.bgcolor("white")

mypen = turtle.Turtle()
mypen.pensize(20)

# mypen.pencolor("purple")
# mypen.circle(-100, 90)
# mypen.left(180)
# mypen.circle(100, 180)

# mypen.penup()
# mypen.goto(0, 19)
# mypen.pendown()
# mypen.left(90)

# mypen.pencolor("blue")
# mypen.circle(-120, 90)
# mypen.left(180)
# mypen.circle(120, 180)

def draw_rainbow(color, Px, Nx, x, y):
    mypen.pencolor(color)
    mypen.circle(Px, 90)
    mypen.left(180)
    mypen.circle(Nx, 180)

    mypen.penup()
    mypen.goto(x, y)
    mypen.pendown()
    mypen.left(90)

# draw_rainbow("purple", -100, 100, 0, 20)
# draw_rainbow("blue", -120, 120, 0, 40)
# draw_rainbow("light green", -140, 140, 0, 60)
# draw_rainbow("yellow", -160, 160, 0, 80)
# draw_rainbow("orange", -180, 180, 0, 100)
# draw_rainbow("red", -200, 200, 0, 120)

color_list = ["purple", "blue", "light green", "yellow", "orange", "red"]

for i in range(6):
    draw_rainbow(color_list[i], -100+(i*20), 100+(i*20), 0, 20+(i*20))

# 0, 20, 40, 60, 80, 100
# 100, 120, 140, 160, 180, 200
# 0, 1, 2, 3, 4, 5
# 20, 40, 60, 80, 100, 120
# 20 + i*20


screen.mainloop()


