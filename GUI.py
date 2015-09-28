"""
2015/XX/XX

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of prompting the user for input & displaying it out on a graphical overlay while allowing user input
"""

# Imports In Module(s) That Will Be Utilized
import turtle
from ASCII import printOutASCII

# Initialize Variables
boardTopLeftX = -250.0
boardTopLeftY = -boardTopLeftX
placePieceRow = 0.0
placePieceColumn = 0.0
moveCounter = 1

# Initialize Board 8x8 Matrix
boardMatrix = [[0 for boardMatrixIndex in range(9)] for boardMatrixIndex in range(9)]

# Initialize The Display Out & The First Turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()
displayOut.bgcolor("#101010")
displayOut.title("Reversi By Group 22")

# Hides The Turtle Pointer
turtle1.hideturtle()

# Sets The Drawing Speed Of The Turtle & The Screen Print Out Delay To 0 (Instantaneous)
turtle1.speed(0)
displayOut.delay(0)


# Function To Print Out The Reversi Table
def printOutTable():
    # Sets The Turtle's Tracer Colour To White
    turtle1.color("white")
    # For Loop To Teleport The Turtle To Coordinates & Print The Reversi Table
    for indexCounter in range(9):
        # Lifts Up The Turtle & Prevents It From Leaving A Trail
        turtle1.up()
        # Teleports The Turtle To The Left Hand Side Of The Next Row
        turtle1.goto(boardTopLeftX, boardTopLeftY - indexCounter * boardTopLeftY / 4)
        # Lowers The Turtle & Allows It To Leave A Trail Again
        turtle1.down()
        # Prints Out The Row's Line
        turtle1.forward(boardTopLeftX * -2)

        # Turns The Turtle Right To Print Out A Vertical Line
        turtle1.right(90)
        # Lifts Up The Turtle & Prevents It From Leaving A Trail
        turtle1.up()
        # Teleports The Turtle To The Top Of The Next Column
        turtle1.goto(boardTopLeftX - indexCounter * boardTopLeftX / 4, boardTopLeftY)
        # Lowers The Turtle & Allows It To Leave A Trail Again
        turtle1.down()
        # Prints Out The Row's Line
        turtle1.forward(boardTopLeftY * 2)
        # Turns The Turtle Back Left To Print Out The Horizontal Line
        turtle1.left(90)
    # Sets The Turtle's Tracer Colour To Black
    turtle1.color("black")


# Function To Check Whether Or Not The X & Y Coordinates Fed In Are Valid
def checkIfValidMove(inputRow, inputColumn):
    # Checks To See Whether Or Not The Coordinates The User Entered Are Within Bounds
    if inputRow <= 8 and inputColumn <= 8 and inputRow >= 1 and inputColumn >= 1:
        # Checks To See Whether Or Not The Entry Index In The Matrix Is Free
        if boardMatrix[inputRow][inputColumn] == 0:
            return True
        else:
            return False
    else:
        return False


# Function To Teleport The Turtle To A Certain Tile (To Print Out The Circle Later)
def teleportToTile(inputRow, inputColumn):
    # Lifts Up The Turtle & Prevents It From Leaving A Trail
    turtle1.up()
    # Teleports To The Relevant Tile
    turtle1.goto(boardTopLeftX - (inputColumn - 0.5) * boardTopLeftX / 4, boardTopLeftY - inputRow * boardTopLeftY / 4)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()


# Function To Add A Piece To The Board
def addPieceToBoard(inputRow, inputColumn, moveCount):
    # Starts The Fill Command (To Fill In The Printed Circle)
    turtle1.begin_fill()

    # If / Else Statement To Check Which Colour To Fill The Circle With (Odd Is Blue & Even Is Red) & It Also Stores Who Occupied The Tile
    if moveCount % 2 == 0:
        # If The Number Is Even, Fills It Blue & Stores That They Occupied It
        turtle1.fillcolor("Red")
        boardMatrix[inputRow][inputColumn] = "Red"
    else:
        # If The Number Is Odd, Fills It Red & Stores That They Occupied It
        turtle1.fillcolor("Blue")
        boardMatrix[inputRow][inputColumn] = "Blue"
        moveCount += 1

    # Prints Out A Circle In The Tile
    turtle1.circle(-boardTopLeftX / 8)
    # Ends The Fill Command
    turtle1.end_fill()


# Calls Function To Print Out The Reversi Table
printOutTable()

# Welcomes The User To The Program
printOutASCII()

# Endless While Loop To Handle The User's Inputted Move
while True:
    # Prompts The User For Their Move's Location & Stores It In Variables (Pop Up Box)
    placePieceRow = int(displayOut.numinput("Piece Row Input. Move Count: " + str(moveCounter), "Row You Would Like To Place A Piece In: ", minval = 1, maxval = 8))
    placePieceColumn = int(displayOut.numinput("Piece Column Input. Move Count: " + str(moveCounter), "Column You Would Like To Place A Piece In: ", minval = 1, maxval = 8))

# Checks To See If The Coordinates Entered Is Valid & Then Performs The Move
    if checkIfValidMove(placePieceRow, placePieceColumn):
        moveCounter += 1
        teleportToTile(placePieceRow, placePieceColumn)
        addPieceToBoard(placePieceRow, placePieceColumn, moveCounter)
    else:
        # Tells The User That The Coordinates Entered Were Invalid
        print("Invalid Move!")

# Closes The Program If The GUI Overlay Is Clicked
displayOut.exitonclick()
