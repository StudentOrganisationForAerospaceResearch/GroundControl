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
from ASCII import printOutASCII

# Initialize global constants (necessary for when functions are called from a different file)
HALF_Board_Width = -250.0
HALF_BOARD_HEIGHT = -HALF_Board_Width
BOARD_OUTLINE_COLOUR = "White"
BOARD_BACKGROUND_COLOUR = "Brown"
PLAYER_1_COLOUR = "White"
PLAYER_2_COLOUR = "Black"

# Initialize global mutable list (index 1 = latest user added piece row, index 2 = latest user added piece column)
playerPieceData = [0, 0]

# Initialize global mutable 8x8 matrix (2D array) to act as the board
boardMatrix = [[0 for boardMatrixIndex in range(9)] for boardMatrixIndex in range(9)]

# Initialize the display out & the first turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()


# Function to print out the ASCII intro to the display overlay & waits 10 seconds before running the program
def printOutIntro():
    teleportToTile(6, 1)
    turtle1.write(printOutASCII(), align="Left", font=("Arial", int(abs(HALF_Board_Width) * 1 / 25)))
    time.sleep(10)
    turtle1.clear()


# Function to print out the reversi table. Clears display before printing and sets color to contrast BG
# Takes no params, accesses global variable BOARD_OUTLINE_COLOUR
def printOutTable():
    turtle1.clear()
    turtle1.color(BOARD_OUTLINE_COLOUR)

    # For loop to teleport the turtle through generating the board. Starts top left
    for indexCounter in range(9):
        # Lift turtle and teleport to left hand side of the following row, top left if first row
        # Then draw line
        turtle1.up()
        turtle1.goto(HALF_Board_Width, HALF_BOARD_HEIGHT - indexCounter * HALF_BOARD_HEIGHT / 4)
        turtle1.down()
        turtle1.forward(-HALF_Board_Width * 2)

        # Turn turtle to print column line, follows same steps as above
        # Then turns the turtle back to the horizontal for the next row
        turtle1.right(90)
        turtle1.up()
        turtle1.goto(HALF_Board_Width - indexCounter * HALF_Board_Width / 4, HALF_BOARD_HEIGHT)
        turtle1.down()
        turtle1.forward(HALF_BOARD_HEIGHT * 2)
        turtle1.left(90)

    turtle1.color("Black")


# Function to check whether coordinates are valid - returns boolean
# Params:
#   inputRow - row number in numerical value
#   inputColumn - column number in numerical value
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


# Function to teleport the turtle to a different tile on the board without leaving a trail (Calculates X & Y coordinates provided tile numbers)
# Params:
#   inputRow - row number in numerical value
#   inputColumn - column number in numerical value
def teleportToTile(inputRow, inputColumn):
    turtle1.up()
    # Takes the floored values of the inputted column (to prevent moving to anywhere inside of a tile besides its center) and subtract 0.5 from it to make sure the turtle will teleport to the tile's center
    # Then Calculates the size of each tile on the board by taking half the board's width and dividing it by 4 (there are 4 tiles of each half of the board)
    # Then the two calculated values are multiplied together to get the raw X coordinate of where that tile would be on the board
    # Then the newly calculated value is taken and subtracted from half the width of the board to get the distance from the vertex to that tile
    # Performs the same calculation for the raw Y coordinate & half the board's height to get the raw Y coordinate however the floored input value is unnecessary due to the turtle resting on the horizontal line all the time
    turtle1.goto((HALF_Board_Width - ((math.floor(inputColumn) - 0.5) * (HALF_Board_Width / 4))),
                 (HALF_BOARD_HEIGHT - (math.floor(inputRow) * (HALF_BOARD_HEIGHT / 4))))
    turtle1.down()


# Function to calculate the tile requested by the coordinates given (Used to convert raw click data)
# Params:
#   inputX - raw X coordinate in decimal value
#   inputY - raw Y coordinate in decimal value
def coordinatesCalculateTile(inputX, inputY):
    # Calculates row and column based on input
    # Takes the inputted raw Y coordinate and subtracts it from half the board's height to get its current row position on the board
    # Then it calculates the height of each tile by taking half the board's height & dividing it by 4, but adding 1 into it due to grid's boundary being considered otherwise
    # Then divides the two calculated values and absolutes them to make sure the resultant value is a positive value
    # Then floors the resultant value to prevent the calculation returning a value that would be partway in a tile
    # Performs the same calculation using the raw X coordinate & half the board's width to get the column value
    calculatedRow = math.floor(abs(((inputY - HALF_BOARD_HEIGHT) / (HALF_BOARD_HEIGHT / 4))) + 1)
    calculatedColumn = math.floor(abs(((inputX - HALF_Board_Width) / (HALF_Board_Width / 4))) + 1)

    # Stores The Row & Column Values Of The Piece That Is Being Added
    playerPieceData[0] = calculatedRow
    playerPieceData[1] = calculatedColumn


# Function to return the the list containing the row and column to which the user added his piece
def getUserPieceData():
    return playerPieceData


# Function to add a piece to the board & store it in the board matrix
# Params:
#   inputRow - row value in numerical value
#   inputColumn - column value in numerical value
#   playerNumber - the numerical value of the move number
def addPieceToBoard(inputRow, inputColumn, playerNumber):
    # Starts the fill method to fill the printed circle
    turtle1.begin_fill()

    # If provided 1, fill piece with PLAYER_1_COLOUR and store that they occupied said space
    # If provided 2, fill piece with PLAYER_2_COLOUR and store that they occupied said space
    if playerNumber == 1:
        turtle1.fillcolor(PLAYER_1_COLOUR)
        boardMatrix[inputRow][inputColumn] = 1
    elif playerNumber == 2:
        turtle1.fillcolor(PLAYER_2_COLOUR)
        boardMatrix[inputRow][inputColumn] = 2

    # Print out circle with radius of 1/16 of board and end fill method
    turtle1.circle(abs(HALF_Board_Width / 8))
    turtle1.end_fill()


# Function to run and call other functions when the GUI is clicked
# Params:
#   inputX - raw x coordinate in numerical value
#   inputY - raw y coordinate in numerical value
def graphicalOverlayClicked(inputX, inputY):
    # Calculate tile clicked
    coordinatesCalculateTile(inputX, inputY)

    # Validate move, then store that a piece has been played and draw the piece (always player piece) in the correct location
    if checkIfValidMove(playerPieceData[0], playerPieceData[1]):
        teleportToTile(playerPieceData[0], playerPieceData[1])
        addPieceToBoard(playerPieceData[0], playerPieceData[1], 1)


# Function to teleport and add the defined colour piece to the board and to the board matrix
# Params:
#   inputRow - row value in numerical value
#   inputColumn - column value coordinate in numerical value
def teleAddPieceToBoard(inputRow, inputColumn, playerNumber):
    playerPieceData[0] = inputRow
    playerPieceData[1] = inputColumn
    teleportToTile(playerPieceData[0], playerPieceData[1])
    addPieceToBoard(playerPieceData[0], playerPieceData[1], playerNumber)


# Function to perform initial setup for the GUI
def performInitialSetup():
    # Resets The Display Overlay & The Turtle & The Click Listener
    displayOut.reset()
    turtle1.reset()
    displayOut.onclick(None)

    displayOut.bgcolor(BOARD_BACKGROUND_COLOUR)
    displayOut.title("Reversi By Group 22")
    # Takes Half the width of the board (global constant) and multiplies it by 2 to get the entire board's width
    # Then calculates 1/8th of the board's width and subtracts it from the total width to provide some empty space on the sides
    # Then does the same calculation for the board's height
    displayOut.setup(abs(((HALF_Board_Width * 2) + (HALF_Board_Width * 0.25))),
                     abs(((HALF_BOARD_HEIGHT * 2) + (HALF_BOARD_HEIGHT * 0.25))))

    # Hides The Turtle & Makes The Animation Speed / Delay Instantaneous
    turtle1.hideturtle()
    turtle1.speed(0)
    displayOut.delay(0)

    # Calls The Functions To Print Out The Intro & Board
    printOutIntro()
    printOutTable()

    # Sets The Function That Will Be Called When The User Clicks On The Screen & A Listener For It
    displayOut.onclick(graphicalOverlayClicked)
    displayOut.listen()

    # Adds The Default Tiles To The Board
    teleAddPieceToBoard(4, 4, 1)
    teleAddPieceToBoard(4, 5, 2)
    teleAddPieceToBoard(5, 4, 2)
    teleAddPieceToBoard(5, 5, 1)


# Main function to run gui separate from other files
def main():
    # Call initial setup, then wait for user action, then loop though wait for user action
    performInitialSetup()
    displayOut.mainloop()


# Calls the main function if the file is called directly
if __name__ == '__main__':
    main()
