"""
2015/09/24

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
The program draws 4 triangles beside each other in the size requested by the user
"""

# Import modules
import turtle
import math

# Method to calculate hypotenuse of triangle using pythagorean theorem
def lengthH(opposite, adjacent):
    return math.sqrt(opposite**2 + adjacent**2)

# Method to calculate upper angle of triangle using arc-sin
def angles(opposite, hypotenuse):
    return math.degrees(math.asin(opposite/hypotenuse))

# Initialize objects
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()

# Makes The "Turtle" Invisible
turtle1.hideturtle()

# Draw 4 triangle asking for input from user
# Calculate triangle params, draw triangle in a circular way, leave pointer at right hand corner of triangle
for i in range(4):
    # Take input
    opposite = math.fabs(float(input("Please enter an integer length for the first leg: ")))
    adjacent = math.fabs(float(input("Please enter an integer length for the second leg: ")))

    hypotenuse = lengthH(opposite, adjacent)

    angle1 = angles(opposite, hypotenuse)
    angle2 = 90 - angle1

    # Draw triangle
    turtle1.forward(opposite)
    turtle1.left(180-angle2)
    turtle1.forward(hypotenuse)
    turtle1.left(180-angle1)
    turtle1.forward(adjacent)
    turtle1.left(90)
    turtle1.forward(opposite) # leave pointer pointing east at the end of the triangle
