import turtle
import math

# Function to calculate coordinates of points for a star
def create_coordinates(radius):
    angle = 90  # Angle between points of the star

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
    coordinates = create_coordinates(radius)

    t.penup()
    t.goto(coordinates[4])
    t.pendown()

    for coord in coordinates:
      t.goto(coord)
      print(coord)

    t.end_fill()

def draw_polygon(t, sides, radius, xx, yy):
  angle = 90  # Angle between points of the star
  coordinates = []
  additional_angle = 360/sides
  print("additional angle ", additional_angle)
  for _ in range(sides):
      x = radius * math.cos(math.radians(angle)) + xx
      y = radius * math.sin(math.radians(angle)) + yy
      coordinates.append((x, y))
      angle += additional_angle
  t.fillcolor('yellow')
  t.begin_fill()
  
  t.penup()
  t.goto(coordinates[sides-1])
  t.pendown()

  for coord in coordinates:
    t.goto(coord)
  t.end_fill()

# Function to draw a circle
def draw_circle(t, radius, x, y):
    t.fillcolor('red')
    t.begin_fill()
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(radius)
    t.end_fill()

# Set up the turtle
screen = turtle.Screen()
screen.setup(1000, 1000)
screen.bgcolor("white")
screen.title("Star Inside a Circle")

turt = turtle.Turtle()
turt.speed(1)

# Set the radius of the circle
circle_radius = 100

# Draw the circle

draw_circle(turt, circle_radius, 0, -100)
# Draw the star inside the circle
draw_star(turt, circle_radius)

turt.penup()
turt.goto(200, 200)
turt.pendown()
draw_circle(turt, circle_radius, 200, 100)
draw_polygon(turt, 5, circle_radius, 200, 200)

turt.penup()
turt.goto(-200, 100)
turt.pendown()
draw_circle(turt, circle_radius, -200, 100)
draw_polygon(turt, 3, circle_radius, -200, 200)


turt.penup()
turt.goto(-200, -200)
turt.pendown()
draw_circle(turt, circle_radius, -200, -200)
draw_polygon(turt, 4, circle_radius, -200, -100)

# Hide the turtle
turt.hideturtle()
# Keep the window open

turtle.done()
