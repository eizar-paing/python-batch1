import turtle
import math

# Function to calculate coordinates of points for a star
def star_coordinates(radius):
    angle = 144  # Angle between points of the star

    coordinates = []
    for _ in range(5):
        x = radius * math.cos(math.radians(angle))
        y = radius * math.sin(math.radians(angle))
        coordinates.append((x, y))
        angle += 144

    return coordinates

# Function to draw a star
def draw_star(t, radius):
    t.fillcolor('yellow')
    t.begin_fill()
    coordinates = star_coordinates(radius)

    t.penup()
    t.goto(coordinates[4])
    t.pendown()

    for coord in coordinates:
        t.goto(coord)
    t.end_fill()

# Function to draw a circle
def draw_circle(t, radius):
    t.fillcolor('red')
    t.begin_fill()
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius)
    t.end_fill()

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Star Inside a Circle")

turt = turtle.Turtle()
turt.speed(1)

# Set the radius of the circle
circle_radius = 100

# Draw the circle

draw_circle(turt, circle_radius)

# Draw the star inside the circle
draw_star(turt, circle_radius)

# Hide the turtle
turt.hideturtle()

# Keep the window open
turtle.done()
