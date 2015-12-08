"""
2015/12/08

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of handling user input & AI responses from a backend to display it onto an overlay
"""
import math
import random
import time
import turtle
import ReversiBoard as backend

# Initialize global constants (necessary for when functions are called from a different file)
HALF_BOARD_WIDTH = -250.0
HALF_BOARD_HEIGHT = -HALF_BOARD_WIDTH
BOARD_OUTLINE_COLOUR = "White"
BOARD_BACKGROUND_COLOUR = "Brown"
PLAYER_1_COLOUR = "White"
PLAYER_2_COLOUR = "Black"

# Initialize the global display out & turtles for the board, pieces, and ghost pieces
displayOut = turtle.Screen()
boardTurtle = turtle.Turtle()
pieceTurtle = turtle.Turtle()
ghostPieceTurtle = turtle.Turtle()


# Function to print out the ASCII intro to the display overlay & waits 10 seconds before running the program
def printOutIntro():
    teleportToTile(4, 0, boardTurtle)
    boardTurtle.write("""
                                Welcome to Reversi!

    Click squares to play your pieces. You are by default white.

    You will have a choice of AIs to play against.

    Please choose the one that you would like.

    Try to get as many pieces as possible in your colour to win.

    Press "S" to save the current game state from the save file

    Press "L" to load the saved game state from the save file
    """, align="Left", font=("Arial", int(abs(HALF_BOARD_WIDTH) * 1 / 20)))
    time.sleep(10)
    boardTurtle.clear()


# Function to print out the Reversi table. Clears display before printing and sets color to contrast background
def printOutTable():
    boardTurtle.clear()
    boardTurtle.color(BOARD_OUTLINE_COLOUR)
    # Teleport the turtle across the display overlay generating the board (starts in the top left corner)
    for indexCounter in range(9):
        # Lift turtle and teleport to left hand side of the following row, top left if first row
        # Then draw line
        boardTurtle.up()
        boardTurtle.goto(HALF_BOARD_WIDTH, HALF_BOARD_HEIGHT - indexCounter * HALF_BOARD_HEIGHT / 4)
        boardTurtle.down()
        boardTurtle.forward(-HALF_BOARD_WIDTH * 2)

        # Turn turtle to print column line, follows same steps as above
        # Then turns the turtle back to the face the original direction for the next row
        boardTurtle.right(90)
        boardTurtle.up()
        boardTurtle.goto(HALF_BOARD_WIDTH - indexCounter * HALF_BOARD_WIDTH / 4, HALF_BOARD_HEIGHT)
        boardTurtle.down()
        boardTurtle.forward(HALF_BOARD_HEIGHT * 2)
        boardTurtle.left(90)
    boardTurtle.color("Black")


# Function to calculate the tile on the board given the raw display overlay coordinates (Used to convert raw click data)
# Params:
#       inputX - raw X coordinate in decimal value
#       inputY - raw Y coordinate in decimal value
def coordinatesCalculateTile(inputX, inputY):
    # Takes the provided Y coordinate and subtracts it from half the board's height to get the current row position
    # Then calculates the height of each tile by taking half the board's height & dividing it by 4
    # Then divides the two calculated values and absolutes them to make sure the resultant value is a positive value
    # Then floors the resultant value to prevent the calculation returning a value that would be partway in a tile
    # Performs the same calculation using the raw X coordinate & half the board's width to get the column value
    calculatedRow = math.floor(abs(((inputY - HALF_BOARD_HEIGHT) / (HALF_BOARD_HEIGHT / 4))))
    calculatedColumn = math.floor(abs(((inputX - HALF_BOARD_WIDTH) / (HALF_BOARD_WIDTH / 4))))
    return [calculatedRow, calculatedColumn]


# Function to teleport the turtle to a different tile on the board without leaving a trail (calculates x & y coordinates
#   provided tile numbers)
# Params:
#       inputRow - row number in numerical value
#       inputColumn - column number in numerical value
#       inputTurtle - the global turtle that will be teleported
def teleportToTile(inputRow, inputColumn, inputTurtle):
    inputTurtle.up()
    # Takes the floored value of the provided column (to prevent moving to anywhere inside of a tile besides its center)
    #  and subtracts 0.5 from it to make sure the turtle will teleport to the tile's center
    # Then calculates the size of each tile on the board by taking half the board's width and dividing it by 4
    #  (there are 4 tiles on each half side of the board)
    # Then the two calculated values are multiplied together to get the raw X coordinate of where that tile would be on
    #  the board
    # Then the newly calculated value is taken and subtracted from half the width of the board to get the distance from
    #  the vertex to that tile
    # Performs the same calculation for the raw Y coordinate & half the board's height to get the raw Y coordinate
    #  however the floored input value is unnecessary due to the turtle resting on the horizontal line all the time
    inputTurtle.goto((HALF_BOARD_WIDTH - ((math.floor(inputColumn + 1) - 0.5) * (HALF_BOARD_WIDTH / 4))),
                     (HALF_BOARD_HEIGHT - (math.floor(inputRow + 1) * (HALF_BOARD_HEIGHT / 4))))
    inputTurtle.down()


# Function to add a piece to the board in the current tile the turtle is located in (to be used alongside the
#  teleportToTile function)
# Params:
#       playerNumber - the numerical value to define which player's tiles are being put down
def addPieceToBoard(playerNumber):
    # If provided 1, fill piece with PLAYER_1_COLOUR (Human)
    # If provided 2, fill piece with PLAYER_2_COLOUR (AI)
    # If provided 3, fill piece with BOARD_BACKGROUND_COLOUR (Ghost Piece)
    if playerNumber == 1:
        pieceTurtle.fillcolor("")
        pieceTurtle.color("")

        pieceTurtle.begin_fill()

        pieceTurtle.color("black")
        pieceTurtle.fillcolor(PLAYER_1_COLOUR)

        pieceTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
        pieceTurtle.end_fill()
    elif playerNumber == 2:
        pieceTurtle.fillcolor("")
        pieceTurtle.color("")

        pieceTurtle.begin_fill()

        pieceTurtle.color("black")
        pieceTurtle.fillcolor(PLAYER_2_COLOUR)

        pieceTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
        pieceTurtle.end_fill()
    elif playerNumber == 3:
        ghostPieceTurtle.fillcolor("")
        ghostPieceTurtle.color("")

        ghostPieceTurtle.begin_fill()

        ghostPieceTurtle.color("black")
        ghostPieceTurtle.fillcolor(BOARD_BACKGROUND_COLOUR)

        ghostPieceTurtle.circle(abs(HALF_BOARD_WIDTH / 8))
        ghostPieceTurtle.end_fill()


# Function to teleport and add the defined colour piece to the board and to the board matrix
# Params:
#       inputRow - row value in numerical value
#       inputColumn - column value coordinate in numerical value
#       playerNumber - numerical value to represent whether it is the AI or Human (value = 1 OR 2) whose piece will be
#        put down or a ghost piece (value = 3)
def teleAddPieceToBoard(inputRow, inputColumn, playerNumber):
    if playerNumber == 1 or playerNumber == 2:
        teleportToTile(inputRow, inputColumn, pieceTurtle)
        addPieceToBoard(playerNumber)
    elif playerNumber == 3:
        teleportToTile(inputRow, inputColumn, ghostPieceTurtle)
        addPieceToBoard(playerNumber)


# Function to loop through and see if there are any valid moves remaining for either the player or the AI (will be used
#  to determine turn skipping / if the game has ended)
# Params:
#       playerArrayInput - move validity array input for the player
#       aiArrayInput - move validity array input for the AI
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


# Function to teleport and add the ghost pieces onto the board
def addGhostPiecesToBoard():
    # Gets the array containing all the valid moves the player can perform, and the board array, and adds ghost pieces
    #  into unoccupied valid move spots
    playerValidMoves = backend.findValids(True)
    currentBoardState = backend.getBoard()
    for rowCounter in range(8):
        for columnCounter in range(8):
            if playerValidMoves[rowCounter][columnCounter] == 1 and currentBoardState[rowCounter][columnCounter] == 0:
                teleAddPieceToBoard(rowCounter, columnCounter, 3)


# Function to rewrite the changed board pieces based on the provided array & comparing + modifying to the original
def updateBoardPieces(inputNewBoardMatrix, inputOldBoardMatrix=[[0 for i in range(8)] for i in range(8)]):
    # Loops through the entire board matrix, comparing entries & adding in changed pieces
    for rowCounter in range(8):
        for columnCounter in range(8):
            if inputOldBoardMatrix[rowCounter][columnCounter] != inputNewBoardMatrix[rowCounter][columnCounter]:
                teleAddPieceToBoard(rowCounter, columnCounter, int(inputNewBoardMatrix[rowCounter][columnCounter]))


# Function to take an input list and perform a deep copy upon it and returns the newly copied list back
#  (only capable of deepcopying on 1D or 2D lists, aliasing would occur on deeper lists)
# Params:
#       inputList - (MANDATORY PARAM) Takes in a list input (1D or 2D) that will be deepcopied
#       finalList - (RECURSIVE PARAM) Takes in the currently populated finalList and uses it to add onto until fully
#        copied
#       hasBeenFullyCopied - (RECURSIVE PARAM) Takes in a boolean that determines whether or not to stop the recursive
#        process (will end in returning the finalList)
#       upperListCounter - (RECURSIVE PARAM) Takes in the current upper list position that is currently being read
#       lowerListCounter - (RECURSIVE PARAM) Takes in the current sublist position that is currently being read
def recursiveListDeepCopy(inputList, finalList=None, hasBeenFullyCopied=False, upperListCounter=0, lowerListCounter=0):
    # Check to see whether or not the recursion should stop and send back the list
    if not hasBeenFullyCopied:
        # Sets the default finalList parameter to be an empty list if nothing was passed (setting a default in the
        #  function call itself would lead to aliasing problems due to lists being mutable otherwise)
        if finalList is None:
            finalList = []
        # Creates a simple list that matches the size of the input array (only looks at the upper list)
        if len(finalList) < len(inputList):
            for counter in range(len(inputList)):
                finalList.append([])
        # Returns an empty list only if it was provided with an empty list
        elif len(inputList) == 0:
            return recursiveListDeepCopy(inputList, finalList, True, upperListCounter, lowerListCounter)
        # Only run if the entire input list has not been iterated across
        if upperListCounter < len(inputList):
            try:
                # Checks to see if the current upper list entry has a sublist or not (causes the except to be called if
                #  there is no sublist under the current spot)
                if len(inputList[upperListCounter]) >= 1:
                    # Check to see if the list has fully been iterated across & copied (updates the end boolean)
                    if (len(inputList) - 1) == upperListCounter and len(
                            inputList[len(inputList) - 1]) == lowerListCounter:
                        return recursiveListDeepCopy(inputList, finalList, True, upperListCounter, lowerListCounter)
                    # Check to see if all the sublist entries have been hit for the current upperlist entry
                    #  (moves onto the next upperlist entry)
                    elif lowerListCounter == len(inputList[upperListCounter]):
                        return recursiveListDeepCopy(inputList, finalList, hasBeenFullyCopied, upperListCounter + 1, 0)
                    # Adds the current sublist value into the final list and calls the recursive method again upon the
                    #  next sublist entry
                    else:
                        finalList[upperListCounter].append(inputList[upperListCounter][lowerListCounter])
                        return recursiveListDeepCopy(inputList, finalList, hasBeenFullyCopied, upperListCounter,
                                                     lowerListCounter + 1)
                # Moves onto the next position in the upper list if the current entry did not have any sublist
                #  (needed for sublisted empty lists)
                elif len(inputList) != upperListCounter:
                    return recursiveListDeepCopy(inputList, finalList, False, upperListCounter + 1, lowerListCounter)
            # Catches TypeError that comes from attempting to read / check for a sublist when none exists
            #  (stores the current upperlist entry and moves onto the next)
            except TypeError:
                finalList[upperListCounter] = inputList[upperListCounter]
                return recursiveListDeepCopy(inputList, finalList, hasBeenFullyCopied, upperListCounter + 1,
                                             lowerListCounter)
        # Check to see whether all the upperlists have been hit and updates the end recursion boolean
        #  (needed in case the last entry was only consisting of an upperlist but no sublists)
        else:
            return recursiveListDeepCopy(inputList, finalList, True, upperListCounter, lowerListCounter)
    # Sends back the newly copied list only when the boolean mentions that the recursive tasks are complete
    elif hasBeenFullyCopied:
        return finalList


# Function to run and call other functions when the GUI is clicked
# Params:
#       inputX - raw x coordinate in numerical value
#       inputY - raw y coordinate in numerical value
def graphicalOverlayClicked(inputX, inputY):
    # Calculates the tile clicked, gets the number of valid moves possible for the player & the AI, and stores the
    #  current board's status (to keep track of updated pieces)
    calculatedCoordinates = coordinatesCalculateTile(inputX, inputY)
    numberOfValidMoves = checkForRemainingValidMoves(recursiveListDeepCopy(backend.findValids(True)),
                                                     recursiveListDeepCopy(backend.findValids(False)))
    oldBoardState = recursiveListDeepCopy(backend.getBoard())
    # Checks to see if the human can perform a move, otherwise skips to the AI, otherwise runs the end game function
    if numberOfValidMoves[0] > 0:
        if 7 >= calculatedCoordinates[0] >= 0 and 7 >= calculatedCoordinates[1] >= 0:
            if (recursiveListDeepCopy(backend.findValids(True))[calculatedCoordinates[0]][calculatedCoordinates[1]]) == 1:
                # Feeds the backend with the user's inputted piece row & column values, and updates the board's pieces,
                #  while removing the now outdated ghost pieces
                backend.playerMove(calculatedCoordinates[0], calculatedCoordinates[1])
                updateBoardPieces(backend.getBoard(), oldBoardState)
                ghostPieceTurtle.clear()

                # Stores the current board's status (to keep track of updated pieces), allows the AI to make a move,
                #  and updates the board based on the changes, and adds new ghost pieces
                oldBoardState = recursiveListDeepCopy(backend.getBoard())
                backend.getAiMove()
                updateBoardPieces(backend.getBoard(), oldBoardState)
                addGhostPiecesToBoard()
    elif numberOfValidMoves[1] > 0:
        # Removes the current ghost pieces, allows the AI to make a move, and updates the board based on the changes,
        #  and adds new ghost pieces
        ghostPieceTurtle.clear()
        backend.getAiMove()
        updateBoardPieces(backend.getBoard(), oldBoardState)
        addGhostPiecesToBoard()
    elif numberOfValidMoves[0] == 0 and numberOfValidMoves[1] == 0:
        pieceCount = [0, 0]
        for rowCounter in range(8):
            for columnCounter in range(8):
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


# Function to import the game's state from a file
def importGameStateFromFile():
    try:
        # Initialize a new list & the save game file reader utility & specifies that it is to be imported from
        saveGameFile = open("Reversi Save Game", "r")
        importedBoard = [[0 for importedMatrixIndex in range(8)] for importedMatrixIndex in range(8)]
        currentIndex = 0
        fileData = saveGameFile.read()
        # Loops through the entire file except last spot & imports it into the temp board matrix, then sets the
        #  game difficulty and closes the save file reader
        for rowCounter in range(8):
            for columnCounter in range(8):
                importedBoard[rowCounter][columnCounter] = int(fileData[currentIndex:currentIndex + 1])
                currentIndex += 1
        backend.setDifficulty(int(fileData[len(fileData) - 1]))
        saveGameFile.close()
        # Sends the newly populated game board to the backend and updates the GUI's game state as well by
        #  first resetting the current board's pieces
        backend.writeBoard(importedBoard)
        pieceTurtle.clear()
        ghostPieceTurtle.clear()
        updateBoardPieces(backend.getBoard())
        addGhostPiecesToBoard()
    except Exception:
        pass


# Function to export the game's current state to a file
def saveGameStateToFile():
    try:
        # Gets the board from the backend, initializes a new save file to write to (overwrites any existing one),
        #  and loops through the board matrix and writes it to the file
        gameBoard = backend.getBoard()
        saveGameFile = open("Reversi Save Game", "w")
        for rowCounter in range(8):
            for columnCounter in range(8):
                saveGameFile.write(str(gameBoard[rowCounter][columnCounter]))
        saveGameFile.write(str(backend.getDifficulty()))
        saveGameFile.close()
    except Exception:
        pass


# Function to get the difficulty of the AI from the player
def getGameDifficulty():
    gameDifficulty = displayOut.textinput("Difficulty",
                                          "How hard would you like the game to be? (1 = Easy, 2 = Moderate, 3 = Agressive, 4 = Extreme) ")
    while gameDifficulty != "1" and gameDifficulty != "2" and gameDifficulty != "3" and gameDifficulty != "4" or gameDifficulty is None:
        gameDifficulty = displayOut.textinput("Difficulty",
                                              "How hard would you like the game to be? (1 = Easy, 2 = Moderate, 3 = Agressive, 4 = Extreme) ")
    return int(gameDifficulty)


# Function that randomly determines whether to allow the AI to make the first move in the game or the player
def performFirstMove():
    # Stores a randomly generated number (either 1 or 2), and if it is 1 skips to the human's turn otherwise allows the
    #  AI to make a move
    randomPlayerGeneration = random.randrange(1, 3)
    if randomPlayerGeneration == 1:
        pass
    elif randomPlayerGeneration == 2:
        backend.getAiMove()


# Function to perform initial setup for the GUI
def performInitialSetup():
    # Resets the display overlay & all the turtles & the click listeners & the piece data & the board matrix
    displayOut.reset()
    boardTurtle.reset()
    pieceTurtle.reset()
    ghostPieceTurtle.reset()
    displayOut.onclick(None)
    displayOut.onkey(None, "l")
    displayOut.onkey(None, "s")
    displayOut.bgcolor(BOARD_BACKGROUND_COLOUR)
    displayOut.title("Reversi By Group Reversi02")
    blankBoard = [[0 for i in range(8)] for i in range(8)]

    # Populates the board with the initial starting pieces & sends it off to the backend
    blankBoard[3][3] = 1
    blankBoard[3][4] = 2
    blankBoard[4][3] = 2
    blankBoard[4][4] = 1
    backend.writeBoard(blankBoard)

    # Scales the display overlay window based on the specified size of the board
    # Takes half the width of the board (global constant) and multiplies it by 2 to get the entire board's width
    # Then calculates 1/8th of the board's width and subtracts it from the total width to have empty spaces on the sides
    # Then does the same calculation for the board's height
    displayOut.setup(abs(((HALF_BOARD_WIDTH * 2) + (HALF_BOARD_WIDTH * 0.25))),
                     abs(((HALF_BOARD_HEIGHT * 2) + (HALF_BOARD_HEIGHT * 0.25))))

    # Hides the turtles & makes the animation speed / delay instantaneous
    pieceTurtle.hideturtle()
    pieceTurtle.speed(0)
    boardTurtle.hideturtle()
    boardTurtle.speed(0)
    ghostPieceTurtle.hideturtle()
    ghostPieceTurtle.speed(0)
    displayOut.delay(0)

    # Calls the functions to print out the intro & board
    printOutIntro()
    printOutTable()

    # Gets the game's difficulty, determine and performs the first random move, and updates the board & ghost pieces
    backend.setDifficulty(getGameDifficulty())
    performFirstMove()
    updateBoardPieces(backend.getBoard())
    addGhostPiecesToBoard()

    # Sets the function that will be called when the user clicks on the screen + for L is pressed + for S is pressed
    displayOut.onkey(importGameStateFromFile, "l")
    displayOut.onkey(saveGameStateToFile, "s")
    displayOut.onclick(graphicalOverlayClicked)
    displayOut.listen()


# Function to handle the end of the game
# Params:
#       inputEndDialogue - the text that will be shown to the user when the game ends
def endGame(inputEndDialogue):
    userGameRestartPrompt = displayOut.textinput(inputEndDialogue, "Would You Like To Restart? (Yes / No): ")
    if userGameRestartPrompt is None or userGameRestartPrompt.lower() != "yes":
        pass
    elif userGameRestartPrompt.lower() == "yes":
        performInitialSetup()


# Main function to run the Reversi game
def main():
    performInitialSetup()
    displayOut.mainloop()


# Calls the main function if the file is called directly
if __name__ == '__main__':
    main()
