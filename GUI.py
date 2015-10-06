"""
2015/XX/XX

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of prompting the user for input & displaying it out on a graphical overlay while allowing user input
"""
import turtle
import time
import math
import random
from ASCII import printOutASCII

# Initialize global constants (necessary for when functions are called from a different file)
halfBoardWidth = -250.0
halfBoardHeight = -halfBoardWidth
boardOutlineColour = "White"
boardBackgroundColour = "Brown"
player1Colour = "White"
player2Colour = "Black"
playerPieceData = [1, 0, 0]

# Initialize board 8x8 matrix (2D array)
boardMatrix = [[0 for boardMatrixIndex in range(9)] for boardMatrixIndex in range(9)]

# Initialize the display out & the first turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()
displayOut.bgcolor(boardBackgroundColour)
displayOut.title("Reversi By Group 22")
displayOut.setup(abs(halfBoardWidth * 2 + halfBoardWidth * 1 / 4), abs(halfBoardHeight * 2 + halfBoardHeight * 1 / 4))

# Function to print out the ASCII intro to the display overlay & waits 10 seconds before running the program
def printOutIntro():
    teleportToTile(6, 1)
    turtle1.write(printOutASCII(), align="Left", font=("Arial", int(abs(halfBoardWidth) * 1 / 25)))
    time.sleep(10)
    turtle1.clear()

# Function to print out the reversi table. Clears display before printing and sets color to contrast BG
# Takes no params, accesses global variable boardOutlineColour
def printOutTable():
    turtle1.clear()
    turtle1.color(boardOutlineColour)

    # For loop to teleport the turtle through generating the board. Starts top left
    for indexCounter in range(9):
        # Lift turtle and teleport to left hand side of the following row, top left if first row
        # Then draw line
        turtle1.up()
        turtle1.goto(halfBoardWidth, halfBoardHeight - indexCounter * halfBoardHeight / 4)
        turtle1.down()
        turtle1.forward(-halfBoardWidth * 2)

        # Turn turtle to print columnal line, follows same steps as above
        # Then turns the turtle back to the horizontal for the next row
        turtle1.right(90)
        turtle1.up()
        turtle1.goto(halfBoardWidth - indexCounter * halfBoardWidth / 4, halfBoardHeight)
        turtle1.down()
        turtle1.forward(halfBoardHeight * 2)
        turtle1.left(90)

    turtle1.color("Black")

# Function to check whether coordinates are valid - returns boolean
# Params:
#   inputRow - x coordinate in numerical value
#   inputColumn - y coordinate in numerical 
# Implied:
#   boardMatrix[8][8] - from global variables. Is mutable, but not changed
def checkIfValidMove(inputRow, inputColumn):
    if inputRow <= 8 and inputColumn <= 8 and inputRow >= 1 and inputColumn >= 1:
        # Checks to see whether the entry index in the matrix is free
        if boardMatrix[inputRow][inputColumn] == 0:
            return True
        else:
            return False
    else:
        return False

# Function to teleport the turtle to a different position without leaving a trail
# Params:
#   inputRow - x coordinate in numerical value
#   inputColumn - y coordinate in numerical value
def teleportToTile(inputRow, inputColumn):
    turtle1.up()
    turtle1.goto(halfBoardWidth - (math.floor(inputColumn) - 0.5) * halfBoardWidth / 4, halfBoardHeight - math.floor(inputRow) * halfBoardHeight / 4)
    turtle1.down()

# Function to calculate the tile requested by the coordinates given (Used to convert raw click Data)
# Params:
#   inputX - x coordinate in numerical value
#   inputY - y coordinate in numerical value
def coordinatesCalculateTile(inputX, inputY):
    # Calculates row and column based on input
    calculatedColumn = math.floor(abs(((inputY - halfBoardHeight) / (halfBoardHeight / 4))) + 1)
    calculatedRow = math.floor(abs(((inputX - halfBoardWidth) / (halfBoardWidth / 4))) + 1)
    
    # Stores The Row & Column Values Of The Piece That Is Being Added
    playerPieceData[1] = calculatedColumn
    playerPieceData[2] = calculatedRow


# Function to return the row at which the user added his piece
def getUserPieceRow():
    return playerPieceData[1]


# Function to return the column at which the user added his piece
def getUserPieceColumn():
    return playerPieceData[2]


# Function to add a piece to the board
# Params:
#   inputRow - x coordinate in numerical value
#   inputColumn - y coordinate in numerical value
#   moveCount - the numerical value of the move number
def addPieceToBoard(inputRow, inputColumn, moveCount):
    # Starts the fill method to fill the printed circle
    turtle1.begin_fill()

    # If move even, fill piece with player1Colour and store that they occupied said space.
    # If move odd, fill piece with player2Color and store that they occupied said space
    if moveCount % 2 == 0:
        turtle1.fillcolor(player1Colour)
        boardMatrix[inputRow][inputColumn] = player1Colour
    else:
        turtle1.fillcolor(player2Colour)
        boardMatrix[inputRow][inputColumn] = player2Colour

    # Print out circle with radius of 1/16 of board and end fill method
    turtle1.circle(abs(halfBoardWidth / 8))
    turtle1.end_fill()

# Function to run and call other functions when the GUI is clicked
# Params:
#   inputX - x coordinate in numerical value
#   inputY - y coordinate in numerical value
def graphicalOverlayClicked(inputX, inputY):
    # Calculate tile clicked
    coordinatesCalculateTile(inputX, inputY)
    
    # Validate move, then store that a piece has been played and draw the piece in the correct location
    if checkIfValidMove(playerPieceData[1], playerPieceData[2]):
        playerPieceData[0] += 1
        teleportToTile(playerPieceData[1], playerPieceData[2])
        addPieceToBoard(playerPieceData[1], playerPieceData[2], playerPieceData[0])

# Function to perform initial setup for the GUI
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


# Main function to run gui separate from other files
def main():
    # Call initial setup, then wait for user action, then loop though wait for user action
    performInitialSetup()
    displayOut.onclick(graphicalOverlayClicked)
    displayOut.listen()
    displayOut.mainloop()

if __name__=='__main__'
    main()

