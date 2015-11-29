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
import ReversiBoard as backend

# Initialize global constants (necessary for when functions are called from a different file)
HALF_BOARD_WIDTH = -250.0
HALF_BOARD_HEIGHT = -HALF_BOARD_WIDTH
BOARD_OUTLINE_COLOUR = "White"
BOARD_BACKGROUND_COLOUR = "Brown"
PLAYER_1_COLOUR = "White"
PLAYER_2_COLOUR = "Black"

# Initialize the global mutable display out & mutable turtles for the board, pieces, and ghost pieces
displayOut = turtle.Screen()
boardTurtle = turtle.Turtle()
pieceTurtle = turtle.Turtle()
ghostPieceTurtle = turtle.Turtle()


# Function to print out the ASCII intro to the display overlay & waits 5 seconds before running the program
def printOutIntro():
    teleportToTile(7, 0, boardTurtle)
    boardTurtle.write(printOutASCII(), align="Left", font=("Arial", int(abs(HALF_BOARD_WIDTH) * 1 / 30)))
    time.sleep(5)
    boardTurtle.clear()


# Function to print out the reversi table. Clears display before printing and sets color to contrast BG
# Takes no params, accesses global variable BOARD_OUTLINE_COLOUR
def printOutTable():
    boardTurtle.clear()
    boardTurtle.color(BOARD_OUTLINE_COLOUR)

    # For loop to teleport the turtle through generating the board. Starts top left
    for indexCounter in range(9):
        # Lift turtle and teleport to left hand side of the following row, top left if first row
        # Then draw line
        boardTurtle.up()
        boardTurtle.goto(HALF_BOARD_WIDTH, HALF_BOARD_HEIGHT - indexCounter * HALF_BOARD_HEIGHT / 4)
        boardTurtle.down()
        boardTurtle.forward(-HALF_BOARD_WIDTH * 2)

        # Turn turtle to print column line, follows same steps as above
        # Then turns the turtle back to the horizontal for the next row
        boardTurtle.right(90)
        boardTurtle.up()
        boardTurtle.goto(HALF_BOARD_WIDTH - indexCounter * HALF_BOARD_WIDTH / 4, HALF_BOARD_HEIGHT)
        boardTurtle.down()
        boardTurtle.forward(HALF_BOARD_HEIGHT * 2)
        boardTurtle.left(90)

    boardTurtle.color("Black")

    
# Function to teleport the turtle to a different tile on the board without leaving a trail (Calculates X & Y coordinates provided tile numbers)
# Params:
#   inputRow - row number in numerical value
#   inputColumn - column number in numerical value
#   inputTurtle - the global turtle that will be being teleported
def teleportToTile(inputRow, inputColumn, inputTurtle):
    inputTurtle.up()
    # Takes the floored values of the inputted column (to prevent moving to anywhere inside of a tile besides its center) and subtract 0.5 from it to make sure the turtle will teleport to the tile's center
    # Then Calculates the size of each tile on the board by taking half the board's width and dividing it by 4 (there are 4 tiles of each half of the board)
    # Then the two calculated values are multiplied together to get the raw X coordinate of where that tile would be on the board
    # Then the newly calculated value is taken and subtracted from half the width of the board to get the distance from the vertex to that tile
    # Performs the same calculation for the raw Y coordinate & half the board's height to get the raw Y coordinate however the floored input value is unnecessary due to the turtle resting on the horizontal line all the time
    inputTurtle.goto((HALF_BOARD_WIDTH - ((math.floor(inputColumn + 1) - 0.5) * (HALF_BOARD_WIDTH / 4))),
                 (HALF_BOARD_HEIGHT - (math.floor(inputRow + 1) * (HALF_BOARD_HEIGHT / 4))))
    inputTurtle.down()

    
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
    calculatedColumn = math.floor(abs(((inputX - HALF_BOARD_WIDTH) / (HALF_BOARD_WIDTH / 4))) + 1)

    # Returns the calculated row & column
    return [calculatedRow, calculatedColumn]


# Function to add a piece to the board in the current tile the turtle is located in (To be used with alongside the teleportToTile function)
# Params:
#   playerNumber - the numerical value of the player
def addPieceToBoard(playerNumber):
    # If provided 1, fill piece with PLAYER_1_COLOUR (Human)
    # If provided 2, fill piece with PLAYER_2_COLOUR (AI)
    # If provided 3, fill piece with BOARD_BACKGROUND_COLOUR (Ghost Piece)
    if playerNumber == 1:
        # Sets the default colour to transparent to prevent accidental fills
        pieceTurtle.fillcolor("")
        pieceTurtle.color("")

        # Starts the fill method to fill the printed circle
        pieceTurtle.begin_fill()

        pieceTurtle.color("black")
        pieceTurtle.fillcolor(PLAYER_1_COLOUR)

        # Print out circle with radius of 1/16 of board and end fill method
        pieceTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
        pieceTurtle.end_fill()
    elif playerNumber == 2:
        # Sets the default colour to transparent to prevent accidental fills
        pieceTurtle.fillcolor("")
        pieceTurtle.color("")

        # Starts the fill method to fill the printed circle
        pieceTurtle.begin_fill()

        pieceTurtle.color("black")
        pieceTurtle.fillcolor(PLAYER_2_COLOUR)

        # Print out circle with radius of 1/16 of board and end fill method
        pieceTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
        pieceTurtle.end_fill()
    elif playerNumber == 3:
        # Sets the default colour to transparent to prevent accidental fills
        ghostPieceTurtle.fillcolor("")
        ghostPieceTurtle.color("")

        # Starts the fill method to fill the printed circle
        ghostPieceTurtle.begin_fill()

        ghostPieceTurtle.color("black")
        ghostPieceTurtle.fillcolor(BOARD_BACKGROUND_COLOUR)

        # Print out circle with radius of 1/16 of board and end fill method
        ghostPieceTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
        ghostPieceTurtle.end_fill()


# Function to loop through and see if there are any valid moves remaining for either the player or the AI (will be used to determine if the game has ended / turns)
# Params:
#   playerArrayInput - move validity array input for the player
#   aiArrayInput - move validity array input for the AI
def checkForRemainingValidMoves(playerArrayInput, aiArrayInput):
    # Index 0 = number of valid moves for the player
    # Index 1 = number of valid moves for the AI
    validMovesCount = [0, 0]
    for rowCounter in range(8):
        for columnCounter in range(8):
            if playerArrayInput[rowCounter][columnCounter] == 1:
                validMovesCount[0] += 1
            if aiArrayInput[rowCounter][columnCounter] == 1:
                validMovesCount[1] += 1
    return validMovesCount


# Function to take an input list and perform a deep copy upon it and return it back (Only capable of deepcopying on 1D or 2D lists, aliasing would occur on deeper lists)
# Params:
#   inputList - (MANDATORY) Takes in a list input (1D or 2D) that will be deepcopied
#   finalList - (RECURSIVE PARAM) Takes in the currently populated finalList and uses it to add onto until fully copied
#   hasBeenFullyCopied - (RECURSIVE PARAM) Takes in a boolean that determines whether or not to stop the recursive process (will end in returning the finalList)
#   upperListCounter - (RECURSIVE PARAM) Takes in the current upper list position that is currently being read
#   lowerListCounter - (RECURSIVE PARAM) Takes in the current sublist position that is currently being read
def recursiveListDeepCopy(inputList, finalList = None, hasBeenFullyCopied = False, upperListCounter = 0, lowerListCounter = 0):
    # Check to see whether or not the recursion should stop and send back the list
    if hasBeenFullyCopied == False:
        # Sets the default finalList parameter to be an empty list if nothing was passed (settings a default in the function call itself would lead to aliasing problems due to lists being mutable otherwise)
        if finalList == None:
            finalList = []

        # Creates a simple list that matches the size of the input array (only looks at the upper list)
        if len(finalList) < len(inputList):
            for counter in range(len(inputList)):
                finalList.append([])
        # Returns an emtpy list only if it was provided with an empty list
        elif len(inputList) == 0:
            return recursiveListDeepCopy(inputList, finalList, True, upperListCounter, lowerListCounter)

        # Only run if the entire input list has not been iterated across
        if upperListCounter < len(inputList):
            try:
                # Checks to see if the current upper list entry has a sublist or not (Causes the except to be called if there is no sublist under the current spot)
                if len(inputList[upperListCounter]) >= 1:
                    # Check to see if the list has fully been iterated across & copied (updates the end recursion boolean)
                    if (len(inputList) - 1) == upperListCounter and len(inputList[len(inputList) - 1]) == lowerListCounter:
                        return recursiveListDeepCopy(inputList, finalList, True, upperListCounter, lowerListCounter)
                    # Check to see if all the sublist entries have been hit for the current upperlist entry (moves onto the next upperlist entry)
                    elif lowerListCounter == len(inputList[upperListCounter]):
                        return recursiveListDeepCopy(inputList, finalList, hasBeenFullyCopied, upperListCounter + 1, 0)
                    # Adds the current sublist value into the final list and calls the recursive method again upon the next sublist entry
                    else:
                        finalList[upperListCounter].append(inputList[upperListCounter][lowerListCounter])
                        return recursiveListDeepCopy(inputList, finalList, hasBeenFullyCopied, upperListCounter, lowerListCounter + 1)
                # Moves onto the next position in the upper list if the current entry did not have any sublist (needed for sublisted empty lists)
                elif len(inputList) != upperListCounter:
                    return recursiveListDeepCopy(inputList, finalList, False, upperListCounter + 1, lowerListCounter)
            # Catches TypeError that comes from attempting to read / check for a sublist when none exists (stores the current upper list entry and moves onto the next)
            except TypeError:
                finalList[upperListCounter] = inputList[upperListCounter]
                return recursiveListDeepCopy(inputList, finalList, hasBeenFullyCopied, upperListCounter + 1, lowerListCounter)
        # Check to see whether all the upper lists have been hit and updates the end recursion boolean (needed in case the last entry was only consisting of an upper but no sublists)
        else:
            return recursiveListDeepCopy(inputList, finalList, True, upperListCounter, lowerListCounter)
    # Sends back the newly copied list only when the boolean mentions that the recursive tasks are complete
    elif hasBeenFullyCopied == True:
        return finalList


# Function to run and call other functions when the GUI is clicked
# Params:
#   inputX - raw x coordinate in numerical value
#   inputY - raw y coordinate in numerical value
def graphicalOverlayClicked(inputX, inputY):
    # Calculate tile clicked
    calculatedCoordinates = coordinatesCalculateTile(inputX, inputY)

    # Gets the number of valid moves possible for the player & the AI
    numberOfValidMoves = checkForRemainingValidMoves(recursiveListDeepCopy(backend.findValids(True)), recursiveListDeepCopy(backend.findValids(False)))

    # Stores the current board's status (to keep track of updated pieces)
    oldBoardState = recursiveListDeepCopy(backend.getBoard())

    # Checks to see if the human can perform a move, otherwise skips to the AI, otherwise runs the end game function
    if numberOfValidMoves[0] > 0:
        if calculatedCoordinates[0] <= 8 and calculatedCoordinates[0] > 0 and calculatedCoordinates[1] <= 8 and calculatedCoordinates[1] > 0:
            if (recursiveListDeepCopy(backend.findValids(True))[calculatedCoordinates[0]][calculatedCoordinates[1]]) == 1:
                # Feeds the backend with the user's inputted piece Row & Column values
                backend.playerMove(calculatedCoordinates[0], calculatedCoordinates[1])

                # Updates the board's pieces based on the newly populated board provided from the backend
                updateBoardPieces(backend.getBoard(), oldBoardState)

                # Removes the now outdated ghost pieces from the board
                ghostPieceTurtle.clear()

                # Stores the current board's status (to keep track of updated pieces)
                oldBoardState = recursiveListDeepCopy(backend.getBoard())

                # Calls the function that will allow the AI to now perform its turn
                backend.getAiMove()

                # Updates the board's pieces based on the newly populated board provided from the backend
                updateBoardPieces(backend.getBoard(), oldBoardState)

                # Adds updated ghost pieces onto the board
                addGhostPiecesToBoard()

    elif numberOfValidMoves[1] > 0:
        # Removes the now outdated ghost pieces from the board
        ghostPieceTurtle.clear()

        # Calls the function that will allow the AI to now perform its turn
        backend.getAiMove()

        # Updates the board's pieces based on the newly populated board provided from the backend
        updateBoardPieces(backend.getBoard(), oldBoardState)

        # Adds updated ghost pieces onto the board
        addGhostPiecesToBoard()
    elif numberOfValidMoves[0] == 0 and numberOfValidMoves[1] == 0:
        pieceCount = [0, 0]
        
        for rowCounter in range(0, 8):
            for columnCounter in range(0, 8):
                if backend.getBoard()[rowCounter][columnCounter] == 1:
                    pieceCount[0] += 1
                elif backend.getBoard()[rowCounter][columnCounter] == 2:
                    pieceCount[1] += 1
                    
        if pieceCount[0] > pieceCount[1]:
            endGame("Player Has Won By " + str(pieceCount[0] - pieceCount[1]) + " Pieces!")
        elif pieceCount[1] > pieceCount[0]:
            endGame("AI Has Won By " + str(pieceCount[1] - pieceCount[0]) + " Pieces!")
        elif pieceCount[0] == pieceCount[1]:
            endGame("Draw, No One Has Won!")


# Function to teleport and add the defined colour piece to the board and to the board matrix
# Params:
#   inputRow - row value in numerical value
#   inputColumn - column value coordinate in numerical value
#   playerNumber - numerical value to represent whether it is the AI or Human (value = 1 OR 2) whose piece will be put down or a ghost piece (value = 3)
def teleAddPieceToBoard(inputRow, inputColumn, playerNumber):
    if playerNumber == 1 or playerNumber == 2:
        teleportToTile(inputRow, inputColumn, pieceTurtle)
        addPieceToBoard(playerNumber)
    elif playerNumber == 3:
        teleportToTile(inputRow, inputColumn, ghostPieceTurtle)
        addPieceToBoard(playerNumber)


# Function to teleport and add the ghost pieces onto the board
def addGhostPiecesToBoard():
    # Gets the array containing all the valid moves the player can perform
    playerValidMoves = backend.findValids(True)

    # Gets the array containing the current board pieces
    currentBoardState = backend.getBoard()

    # Adds the ghost pieces to the board where there is a valid move opportunity
    for rowCounter in range(8):
        for columnCounter in range(8):
            if playerValidMoves[rowCounter][columnCounter] == 1 and currentBoardState[rowCounter][columnCounter] == 0:
                teleAddPieceToBoard(rowCounter, columnCounter, 3)


# Function to export the game's current state to a file
def saveGameStateToFile():
    try:
        # Gets the board from the backend and stores a local copy
        gameBoard = backend.getBoard()

        # Initialize a save game file & the save game file writer utility (overwrites any existing file) & specifies that it is to be written to
        saveGameFile = open("Reversi Save Game", "w")

        # Loops through the entire board matrix & writes it to the file
        for rowCounter in range(0, 8):
            for columnCounter in range(0, 8):
                saveGameFile.write(str(gameBoard[rowCounter][columnCounter]))
        saveGameFile.write(backend.getDifficulty())

        # Closes the save game file writer utility
        saveGameFile.close()
    except Exception as e:
        pass


# Function to import the game's state from a file
def importGameStateFromFile():
    try:
        # Initialize a new list & the save game file reader utility & specifies that it is to be imported from
        saveGameFile = open("Reversi Save Game", "r")
        importedBoard = [[0 for importedMatrixIndex in range(8)] for importedMatrixIndex in range(8)]
        currentIndex = 0
        fileData = saveGameFile.read()

        # Loops through the entire file except last spot & imports it into the temp board matrix
        for rowCounter in range(0, 8):
            for columnCounter in range(0, 8):
                importedBoard[rowCounter][columnCounter] = int(fileData[currentIndex:currentIndex + 1])
                currentIndex += 1
        
        #get and set game difficulty
        backend.setDifficulty(int(fileData[len(filedata)-1]))
        
        # Closes the save game file reader utility
        saveGameFile.close()

        # Sends the newly populated game board to the backend and updates the GUI's game state as well by first resetting the current board's pieces
        backend.writeBoard(importedBoard)
        pieceTurtle.clear()
        ghostPieceTurtle.clear()
        updateBoardPieces(backend.getBoard())
        addGhostPiecesToBoard()
    except Exception as e:
        pass


# Function to rewrite the changed board pieces based on the provided array & comparing + modifying to the original
def updateBoardPieces(inputNewBoardMatrix, inputOldBoardMatrix = [[0 for i in range(8)] for i in range(8)]):
    # Loops through the entire board matrix, comparing entries & adding in changed pieces
    for rowCounter in range(0, 8):
        for columnCounter in range(0, 8):
            if inputOldBoardMatrix[rowCounter][columnCounter] != inputNewBoardMatrix[rowCounter][columnCounter]:
                teleAddPieceToBoard(rowCounter, columnCounter, int(inputNewBoardMatrix[rowCounter][columnCounter]))


# Function that randomly determines whether to allow the AI to make the first move in the game or the player
def performFirstMove():
    # Stores a randomly generated number (either 1 or 2)
    randomPlayerGeneration = random.randrange(1, 3)

    # If the generated number is 1 does nothing (Human is automatically given the first turn when the GUI starts taking in clicks)
    if randomPlayerGeneration == 1:
        pass
    # If the generated number is 2 performs an AI move
    elif randomPlayerGeneration == 2:
        backend.aiMove()


# Function to handle the end of the game
def endGame(inputEndDialogue):
    userGameRestartPrompt = displayOut.textinput(inputEndDialogue, "Would You Like To Restart? (Yes / No): ")
    if userGameRestartPrompt is None or userGameRestartPrompt.lower() != "yes":
        pass
    elif userGameRestartPrompt.lower() == "yes":
        performInitialSetup()


# Function to perform initial setup for the GUI
def performInitialSetup():
    # Resets The Display Overlay & All The Turtles & The Click Listeners & The Piece Data & The Board Matrix
    displayOut.reset()
    boardTurtle.reset()
    pieceTurtle.reset()
    ghostPieceTurtle.reset()
    displayOut.onclick(None)
    displayOut.onkey(None, "l")
    displayOut.onkey(None, "s")
    blankBoard = [[0 for i in range(8)] for i in range(8)]

    # Populates the board with the initial starting pieces & sends it off to the backend
    blankBoard[3][3] = 1
    blankBoard[3][4] = 2
    blankBoard[4][3] = 2
    blankBoard[4][4] = 1
    backend.writeBoard(blankBoard)

    displayOut.bgcolor(BOARD_BACKGROUND_COLOUR)
    displayOut.title("Reversi By Group 22")
    # Takes Half the width of the board (global constant) and multiplies it by 2 to get the entire board's width
    # Then calculates 1/8th of the board's width and subtracts it from the total width to provide some empty space on the sides
    # Then does the same calculation for the board's height
    displayOut.setup(abs(((HALF_BOARD_WIDTH * 2) + (HALF_BOARD_WIDTH * 0.25))),
                     abs(((HALF_BOARD_HEIGHT * 2) + (HALF_BOARD_HEIGHT * 0.25))))

    # Hides The Turtles & Makes The Animation Speed / Delay Instantaneous
    pieceTurtle.hideturtle()
    pieceTurtle.speed(0)
    boardTurtle.hideturtle()
    boardTurtle.speed(0)
    ghostPieceTurtle.hideturtle()
    ghostPieceTurtle.speed(0)
    displayOut.delay(0)

    # Calls The Functions To Print Out The Intro & Board
    printOutIntro()
    printOutTable()

    # Calls The Function To Randomly Determine & Allows Either The Human Or The AI To Play The First Piece
    performFirstMove()

    # Adds The Default Tiles To The Board
    updateBoardPieces(backend.getBoard())

    # Adds the ghost pieces to the board
    addGhostPiecesToBoard()
	
	#get game difficulty
    gameDifficulty = int(displayOut.textinput("Difficulty", "How hard would you like the game to be? (1 = Easy, 2 = Moderate, 3 = Hard) "))
    
    while gameDifficulty != 1 and gameDifficulty != 2 and gameDifficulty != 3:
        gameDifficulty = int(displayOut.textinput("Difficulty", "How hard would you like the game to be? (1 = Easy, 2 = Moderate, 3 = Hard) "))
    backend.setDifficulty(gameDifficulty)

    # Sets The Function That Will Be Called When The User Clicks On The Screen + For When L Is Pressed + For When S Is Pressed & Listeners For Them
    displayOut.onkey(importGameStateFromFile, "l")
    displayOut.onkey(saveGameStateToFile, "s")
    displayOut.onclick(graphicalOverlayClicked)
    displayOut.listen()


# Main function to run the GUI separate from other files
def main():
    # Call initial setup, then wait for user action, then loop though wait for user action
    performInitialSetup()
    displayOut.mainloop()


# Calls the main function if the file is called directly
if __name__ == '__main__':
    main()
