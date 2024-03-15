import datetime as dt
import time
import turtle

screen = turtle.Screen()
screen.bgcolor("yellow")

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

turtle1.color("black")

for i in range(2):
  turtle1.forward(200)
  turtle1.left(90)
  turtle1.forward(80)
  turtle1.left(90)
turtle1.hideturtle()

secs = dt.datetime.now().second
mins = dt.datetime.now().minute
hrs = dt.datetime.now().hour

turtle2.penup()
turtle2.goto(20, 25)
turtle2.pendown()
turtle2.hideturtle()

while True:
  turtle2.clear()
  turtle2.write(str(hrs).zfill(2) + ":" + str(mins).zfill(2) + ":" + str(secs).zfill(2),
  font=("Callibri Narrow", 40, "bold"))
  time.sleep(1)
  secs += 1
  if secs == 60:
    secs = 0
    mins += 1
  if mins == 60:
    mins = 0
    hrs += 1
  if hrs == 13:
    hrs = 1

turtle.done()