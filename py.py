import turtle
import math

# Convert cm to pixels (approximation)
cm_to_pixels = 37.8
radius_in_pixels = 5 * cm_to_pixels
small_radius_in_pixels = 1 * cm_to_pixels  # Small circle radius in pixels

# Function to draw a star
def draw_star(turtle, size):
    turtle.begin_fill()
    for _ in range(5):
        turtle.forward(size)
        turtle.right(144)
    turtle.end_fill()

# Function to draw stars around the circle
def draw_stars(turtle, radius):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color('blue')

    num_stars = 12  # Number of stars around the circle
    angle_step = 360 / num_stars
    star_size = small_radius_in_pixels * 0.6  # Adjusted size for stars

    for _ in range(num_stars):
        turtle.penup()
        turtle.goto(0, 0)  # Go to center
        turtle.setheading(angle_step * _)  # Rotate to the angle
        turtle.forward(radius - small_radius_in_pixels * 1.2)  # Move to edge of large circle
        turtle.pendown()

        turtle.fillcolor('blue')
        draw_star(turtle, star_size)  # Draw a star

# Function to draw smaller triangles around the circle
def draw_triangles(turtle, radius):
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()
    turtle.color('yellow')

    num_triangles = 12  # Number of triangles around the circle
    angle_step = 360 / num_triangles
    triangle_side = small_radius_in_pixels  # Adjusted side length for smaller triangles

    for _ in range(num_triangles):
        turtle.penup()
        turtle.goto(0, 0)  # Go to center
        turtle.setheading(angle_step * _)  # Rotate to the angle
        turtle.forward(radius - small_radius_in_pixels)  # Move to edge of large circle
        turtle.pendown()
        
        turtle.fillcolor('yellow')
        turtle.begin_fill()

        for _ in range(3):  # Draw a smaller triangle
            turtle.forward(triangle_side)  # Side length of the triangle
            turtle.left(120)  # Turn to next side

        turtle.end_fill()
        turtle.penup()
        turtle.goto(0, 0)

# Function to draw concentric circles with different colors
def draw_concentric_circles(turtle, outer_radius, num_circles):
    # List of colors to use for concentric circles
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet', 'purple', 'pink', 'brown']
    
    step = (outer_radius - small_radius_in_pixels) / num_circles  # Step size between circles
    for i in range(num_circles):
        radius = outer_radius - i * step
        turtle.penup()
        turtle.goto(0, -radius)  # Move to the correct position
        turtle.pendown()
        turtle.color(colors[i % len(colors)])  # Cycle through colors
        
        turtle.begin_fill()  # Begin filling the circle
        turtle.circle(radius)  # Draw the circle
        turtle.end_fill()  # End filling the circle

# Function to draw a small circular flower design inside the small circle
def draw_circular_flower(turtle, radius):
    turtle.penup()
    turtle.goto(0, -radius)  # Move to the center of the small circle
    turtle.pendown()
    num_petals = 6
    petal_length = radius * 0.8
    petal_width = radius * 0.4

    for _ in range(num_petals):
        turtle.penup()
        turtle.goto(0, 0)  # Move to center
        turtle.setheading(360 / num_petals * _)  # Rotate to the next petal position
        turtle.forward(radius * 0.2)  # Move to the starting point for petal
        turtle.pendown()

        turtle.fillcolor('pink')
        turtle.begin_fill()

        turtle.circle(petal_width, 180)  # Draw half petal
        turtle.left(90)
        turtle.forward(petal_length)
        turtle.left(90)
        turtle.circle(petal_width, 180)  # Draw the other half of the petal

        turtle.end_fill()

    # Draw the center of the flower with red color
    turtle.penup()
    turtle.goto(7, 2 )  # Move to the center of the flower
    turtle.pendown()
    turtle.fillcolor('red')
    turtle.begin_fill()
    turtle.circle(radius * 0.2)  # Draw a small circle at the center
    turtle.end_fill()

# Function to draw an umbrella
def draw_umbrella(turtle):
    turtle.penup()
    turtle.goto(-400, -200)  # Move to starting position for umbrella
    turtle.pendown()

    # Draw the canopy of the umbrella (semi-circle)
    turtle.color('blue')
    turtle.begin_fill()
    turtle.setheading(90)  # Point the turtle to the left
    turtle.circle(80, 180)  # Draw a semi-circle with radius 80
    turtle.end_fill()

    
    # Draw the handle of the umbrella
    turtle.penup()
    turtle.goto(-480, -200)  # Move to starting position for handle
    turtle.pendown()
    turtle.color('brown')
    turtle.pensize(10)
    turtle.setheading(-90)  # Point the turtle downwards
    turtle.forward(100)

# Set up the screen and turtle
screen = turtle.Screen()
circle_turtle = turtle.Turtle()
circle_turtle.speed(300)  # Adjust speed for better visibility

# Draw the larger circle with concentric circles
draw_concentric_circles(circle_turtle, radius_in_pixels, 10)  # 10 concentric circles

# Draw the larger circle outline
circle_turtle.penup()
circle_turtle.goto(0, -radius_in_pixels)  # Move to starting position
circle_turtle.pendown()
circle_turtle.circle(radius_in_pixels)

# Draw the small circle in the middle
circle_turtle.penup()
circle_turtle.goto(0, -small_radius_in_pixels)  # Move to starting position for small circle
circle_turtle.pendown()
circle_turtle.fillcolor('green')
circle_turtle.begin_fill()
circle_turtle.circle(small_radius_in_pixels)
circle_turtle.end_fill()

# Draw the circular flower pattern inside the small circle
draw_circular_flower(circle_turtle, small_radius_in_pixels)

# Draw triangles around the large circle
draw_triangles(circle_turtle, radius_in_pixels)

# Draw stars around the large circle
draw_stars(circle_turtle, radius_in_pixels)

# Draw the umbrella on the left side
draw_umbrella(circle_turtle)

# Function to write text at the top side
def write_text(turtle, text):
    turtle.penup()
    turtle.goto(0, radius_in_pixels + 50)  # Position above the larger circle
    turtle.pendown()
    turtle.color('black')
    turtle.write(text, align="center", font=("Arial", 24, "bold"))

# Add this function call after drawing the circles and shapes
write_text(circle_turtle, "Happy Onam")

# Finish drawing
turtle.done()
