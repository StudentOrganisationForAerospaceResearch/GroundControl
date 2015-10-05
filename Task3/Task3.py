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
import time

# Initialize Variables
halfBoardWidth = -250.0
halfBoardHeight = -halfBoardWidth
boardOutlineColour = "White"
boardBackgroundColour = "Brown"
player1Colour = "White"
player2Colour = "Black"
playerPieceCoordinates = [0, 0]

# Initialize Board 8x8 Matrix
boardMatrix = [[0 for boardMatrixIndex in range(9)] for boardMatrixIndex in range(9)]

# Initialize The Display Out & The First Turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()
turtle1.hideturtle()
displayOut.bgcolor(boardBackgroundColour)
displayOut.title("Reversi By Group 22")
displayOut.setup(abs(halfBoardWidth * 2 + halfBoardWidth * 1 / 4), abs(halfBoardHeight * 2 + halfBoardHeight * 1 / 4))

# Sets The Drawing Speed Of The Turtle & The Screen Print Out Delay To 0 (Instantaneous)
turtle1.speed(0)
displayOut.delay(0)


# Function To Print Out The Reversi Table
def printOutTable():
    # Clears Out The Display Overlay Before Printing Out The Table
    turtle1.clear()
    # Sets The Turtle's Tracer Colour To The Defined Colour
    turtle1.color(boardOutlineColour)
    # For Loop To Teleport The Turtle To Coordinates & Print The Reversi Table
    for indexCounter in range(9):
        # Lifts Up The Turtle & Prevents It From Leaving A Trail
        turtle1.up()
        # Teleports The Turtle To The Left Hand Side Of The Next Row
        turtle1.goto(halfBoardWidth, halfBoardHeight - indexCounter * halfBoardHeight / 4)
        # Lowers The Turtle & Allows It To Leave A Trail Again
        turtle1.down()
        # Prints Out The Row's Line
        turtle1.forward(-halfBoardWidth * 2)

        # Turns The Turtle Right To Print Out A Vertical Line
        turtle1.right(90)
        # Lifts Up The Turtle & Prevents It From Leaving A Trail
        turtle1.up()
        # Teleports The Turtle To The Top Of The Next Column
        turtle1.goto(halfBoardWidth - indexCounter * halfBoardWidth / 4, halfBoardHeight)
        # Lowers The Turtle & Allows It To Leave A Trail Again
        turtle1.down()
        # Prints Out The Row's Line
        turtle1.forward(halfBoardHeight * 2)
        # Turns The Turtle Back Left To Print Out The Horizontal Line
        turtle1.left(90)
    # Sets The Turtle's Tracer Colour To Black
    turtle1.color("Black")


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
    turtle1.goto(halfBoardWidth - (inputColumn - 0.5) * halfBoardWidth / 4, halfBoardHeight - inputRow * halfBoardHeight / 4)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()


# Function To Return The Row The User Added His Piece To
def getUserPieceRow():
    return playerPieceCoordinates[0]


# Function To Return The Column The User Added His Piece To
def getUserPieceColumn():
    return playerPieceCoordinates[1]


# Function To Add A Piece To The Board
def addPieceToBoard(inputRow, inputColumn, moveCount):
    # Starts The Fill Command (To Fill In The Printed Circle)
    turtle1.begin_fill()

    # If / Else Statement To Check Which Colour To Fill The Circle With & Also Stores Who Occupied The Tile
    if moveCount % 2 == 0:
        # If The Number Is Even (Player 1), Fills It The Defined Colour & Stores That They Occupied It
        turtle1.fillcolor(player1Colour)
        boardMatrix[inputRow][inputColumn] = player1Colour
    else:
        # If The Number Is Odd (Player 2), Fills It The Defined Colour & Stores That They Occupied It
        turtle1.fillcolor(player2Colour)
        boardMatrix[inputRow][inputColumn] = player2Colour

    # Prints Out A Circle In The Tile
    turtle1.circle(abs(halfBoardWidth / 8))
    # Ends The Fill Command
    turtle1.end_fill()


# Main Function To Run The GUI
def main():
    # Initialize A Move Counter (Will Be Used To Determine Whose Turn It Is & Which Colour Piece To Place Down)
    moveCounter = 1

    # Calls Function To Print Out The Reversi Table
    printOutTable()

    # Endless While Loop To Handle The User's Inputted Move
    while True:
        # Prompts The User For Their Move's Location & Stores It In Variables (Pop Up Box)
        placePieceRow = int(input("Row You Would Like To Place A Piece In: "))
        placePieceColumn = int(input("Column You Would Like To Place A Piece In: "))

        # Checks To See If The Coordinates Entered Is Valid & Then Performs The Move & Stores The Coordinates
        if checkIfValidMove(placePieceRow, placePieceColumn):
            moveCounter += 1
            teleportToTile(placePieceRow, placePieceColumn)
            addPieceToBoard(placePieceRow, placePieceColumn, moveCounter)
            # Stores The Row & Column Values Of The Piece That Is Being Added
            playerPieceCoordinates[0] = placePieceRow
            playerPieceCoordinates[1] = placePieceColumn

    # Closes The Program If The GUI Overlay Is Clicked
    displayOut.exitonclick()


# Calls The Main Function To Run The GUI
main()
