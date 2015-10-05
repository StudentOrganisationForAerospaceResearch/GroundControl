"""
2015/09/22

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
The Programs Draws A Circle, With A Semi Circle Smile, And Stamps The Circle Turtle Graphics Pointer As Eyes
"""

# Imports In The Turtle Graphics Module
import turtle

"""
PLAY WITH ME AND CHANGE MY SIZE
"""
radius = 100

# Initialize The Display Out
# Initialize The First "Turtle"
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()

# Set The Radius Of The Shape to be 1/50 of the radius of the face
turtle1.shapesize(radius / 50, radius / 50)

# Makes The "Turtle" Invisible
turtle1.hideturtle()

# Defines The Shape Of The Turtle Graphics Pointer
turtle1.shape("circle")

# Create A Circle With The Diameter Of radius * 2
turtle1.circle(radius)

# Turns The "Turtle" Left
turtle1.left(90)

# Does Not Allow The "Turtle" To Leave A Trail (Lifts It Up)
turtle1.up()

# Moves The "Turtle" upwards 1/4 of the face's height
turtle1.forward(radius / 2)

# Allows The "Turtle" To Leave A Trail Again (Drops It Down)
turtle1.down()

# Turns The "Turtle" Right
turtle1.right(90)

# Traces The Right, Turns Around, And Then Left Half Of The Circle
# Params: (radius, extent)
# Implied: Starts from coordinate (0, radius) Pointing Right
#          Starts 1/4 of the face up
turtle1.circle(radius, 50)
turtle1.left(180)
turtle1.circle(-radius, 100)

# Turns The "Turtle" 90 Degrees Right
turtle1.right(90)

# Does Not Allow The "Turtle" To Leave A Trail (Lifts It Up)
turtle1.up()

# Moves The "Turtle" 2/3 up the circle and to the left half of the radius - 5
turtle1.goto(-radius/2 + radius / 10, (radius * 4) / 3)

# Stamps / Leaves Behind A Image Of The "Turtle" Pointer
turtle1.stamp()

# Turns The "Turtle" 2/3 up the circle and to the right half of the radius - 5
turtle1.goto(radius/2 - radius / 10, (radius * 4) / 3)

# Stamps / Leaves Behind A Image Of The "Turtle" Pointer
turtle1.stamp()

# Closes The Display Overlay When Clicked
displayOut.exitonclick()
