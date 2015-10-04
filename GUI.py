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
import math
import random
from ASCII import printOutASCII

# Initialize Variables
halfBoardWidth = -250.0
halfBoardHeight = -halfBoardWidth
boardOutlineColour = "White"
boardBackgroundColour = "Brown"
player1Colour = "White"
player2Colour = "Black"
playerPieceData = [1, 0, 0]

# Initialize Board 8x8 Matrix
boardMatrix = [[0 for boardMatrixIndex in range(9)] for boardMatrixIndex in range(9)]

# Initialize The Display Out & The First Turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()
displayOut.bgcolor(boardBackgroundColour)
displayOut.title("Reversi By Group 22")
displayOut.setup(abs(halfBoardWidth * 2 + halfBoardWidth * 1 / 4), abs(halfBoardHeight * 2 + halfBoardHeight * 1 / 4))


# Function To Print Out The ASCII Intro To The Display Overlay & Waits 10 Seconds Before Running The Program
def printOutIntro():
    teleportToTile(6, 1)
    turtle1.write(printOutASCII(), align="Left", font=("Arial", int(abs(halfBoardWidth) * 1 / 25)))
    time.sleep(10)
    turtle1.clear()


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
    turtle1.goto(halfBoardWidth - (math.floor(inputColumn) - 0.5) * halfBoardWidth / 4, halfBoardHeight - math.floor(inputRow) * halfBoardHeight / 4)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()


# Function To Calculate The Tile Based On The Provided Coordinates (Used To Convert Raw Click Data)
def coordinatesCalculateTile(inputX, inputY):
    # Calculates The Row Based On The X Coordinate Provided
    calculatedRow = math.floor(abs(((inputY - halfBoardHeight) / (halfBoardHeight / 4))) + 1)
    # Calculates The Column Based On The Y Coordinate Provided
    calculatedColumn = math.floor(abs(((inputX - halfBoardWidth) / (halfBoardWidth / 4))) + 1)
    # Stores The Row & Column Values Of The Piece That Is Being Added
    playerPieceData[1] = calculatedRow
    playerPieceData[2] = calculatedColumn


# Function To Return The Row The User Added His Piece To
def getUserPieceRow():
    return playerPieceData[1]


# Function To Return The Column The User Added His Piece To
def getUserPieceColumn():
    return playerPieceData[2]


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


# Function To Run & Call Other Functions When The GUI Overlay Is Clicked
def graphicalOverlayClicked(inputX, inputY):
    coordinatesCalculateTile(inputX, inputY)
    if checkIfValidMove(playerPieceData[1], playerPieceData[2]):
        playerPieceData[0] += 1
        teleportToTile(playerPieceData[1], playerPieceData[2])
        addPieceToBoard(playerPieceData[1], playerPieceData[2], playerPieceData[0])


# Function To Perform The Initial Setup Tasks For The GUI
def performInitialSetup():
    # Resets The Display Overlay & The Turtle
    displayOut.reset()
    turtle1.reset()
    # Hides The Turtle & Makes The Animation Speed / Delay Instantaneous
    turtle1.hideturtle()
    turtle1.speed(0)
    displayOut.delay(0)
    # Calls The Functions To Print Out The Intro & Board
    printOutIntro()
    printOutTable()
    # Adds The Default Tiles To The Board
    teleportToTile(4, 4)
    addPieceToBoard(4, 4, 1)
    teleportToTile(4, 5)
    addPieceToBoard(4, 5, 2)
    teleportToTile(5, 4)
    addPieceToBoard(5, 4, 2)
    teleportToTile(5, 5)
    addPieceToBoard(5, 5, 1)
    # Randomly Allows Either Player 1 Or Player 2 To Go First
    playerPieceData[0] = random.randint(1, 2)


# Main Function To Run The GUI
def main():
    # Calls The Function To Perform The Initial Setup Of The Board
    performInitialSetup()

    # Calls A Function When A Spot On The Board Is Clicked (Handles Placing The Tiles)
    displayOut.onclick(graphicalOverlayClicked)

    # Listens To User Input From The GUI
    displayOut.listen()

    # Loops Through The Main Loop Endlessly To Keep Getting User Input From The GUI
    displayOut.mainloop()


# Calls The Main Function To Run The GUI
main()

