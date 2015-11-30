"""
2015/XX/XX

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of handing all the data & handling all move related functions and calls to the AI
"""
from AI import AI

# initializes the 8x8 reversi board and assigns a value of 0 to every square.
# 0 = Empty square
# 1 = White piece
# 2 = black piece
global validMoves
global board
board = [[0 for i in range(8)] for i in range(8)]
validMoves = [[0 for i in range(8)] for i in range(8)]

# set the game difficulty with a default of easy
global game_difficulty


# Modifies the validMoves Array, placing a 1 in every place the defined player can legally place a move.
# PARAMS:
#     userTurn - The player to play
def findValids(userTurn):
    for x in range(0, 8):
        for y in range(0, 8):
            if __isValid(x, y, userTurn):
                validMoves[x][y] = 1

            else:
                validMoves[x][y] = 0

    return validMoves


# Determines if a given square is a valid move.
# PARAMS:
#     playersTurn - True when it is the human player's turn.
#     x - The x position being checked
#     y - The y position being checked.
#
# RETURN:
#     Boolean, true when the direction searched finds a valid move.
def __isValid(x, y, userTurn):
    isValid = False
    scan = 1

    if userTurn:
        player = 1
        opponent = 2
    else:
        player = 2
        opponent = 1

    if board[x][y] == 0:
        if y >= 0 and board[x][y - 1] == opponent:
            while board[x][y - scan] == opponent and (y - scan >= 1):
                scan += 1
                currentIndex = board[x][y - scan]

                if currentIndex == player:
                    isValid = True

            scan = 1
        if y < 7 and board[x][y + 1] == opponent:
            while board[x][y + scan] == opponent and (y + scan <= 6):
                scan += 1
                currentIndex = board[x][y + scan]

                if currentIndex == player:
                    isValid = True

            scan = 1

        if x > 0 and board[x - 1][y] == opponent:
            while board[x - scan][y] == opponent and (x - scan >= 1):
                scan += 1
                currentIndex = board[x - scan][y]

                if currentIndex == player:
                    isValid = True

            scan = 1

        if x < 7 and board[x + 1][y] == opponent:
            while board[x + scan][y] == opponent and (x + scan <= 6):
                scan += 1
                currentIndex = board[x + scan][y]

                if currentIndex == player:
                    isValid = True

            scan = 1

        if x > 0 and y > 0 and board[x - 1][y - 1] == opponent:
            while board[x - scan][y - scan] == opponent and (x - scan >= 1 and y - scan >= 1):
                scan += 1
                currentIndex = board[x - scan][y - scan]

                if currentIndex == player:
                    isValid = True

            scan = 1

        if x > 0 and y < 7 and board[x - 1][y + 1] == opponent:
            while board[x - scan][y + scan] == opponent and (x - scan >= 1 and y + scan <= 6):
                scan += 1
                currentIndex = board[x - scan][y + scan]

                if currentIndex == player:
                    isValid = True

            scan = 1

        if x < 7 and y > 1 and board[x + 1][y - 1] == opponent:
            while board[x + scan][y - scan] == opponent and (x + scan <= 6 and y - scan >= 1):
                scan += 1
                currentIndex = board[x + scan][y - scan]

                if currentIndex == player:
                    isValid = True

            scan = 1

        if x < 7 and y < 7 and board[x + 1][y + 1] == opponent:
            while board[x + scan][y + scan] == opponent and (x + scan <= 6 and y + scan <= 6):
                scan += 1
                currentIndex = board[x + scan][y + scan]

                if currentIndex == player:
                    isValid = True
    return isValid


# Flips opponent's pieces to the current player's pieces.
# PARAMS:
#         x - x coordinate of the placed piece.
#         y - y coordinate of the placed piece
#         playersTurn - Boolean, true when it is the player's Turn.
def __flipPieces(x, y, playersTurn):
    if playersTurn:
        player = 1
        opponent = 2
    else:
        player = 2
        opponent = 1
    scan = 1

    if y >= 0 and board[x][y - 1] == opponent:
        while board[x][y - scan] == opponent and (y - scan >= 1):
            scan += 1
            currentIndex = board[x][y - scan]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x][y - i] = player
        scan = 1

    if y < 7 and board[x][y + 1] == opponent:
        while board[x][y + scan] == opponent and (y + scan <= 6):
            scan += 1
            currentIndex = board[x][y + scan]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x][y + i] = player
        scan = 1

    if x > 0 and board[x - 1][y] == opponent:

        while board[x - scan][y] == opponent and (x - scan >= 1):
            scan += 1
            currentIndex = board[x - scan][y]

            if currentIndex == player:

                for i in range(0, scan):
                    board[x - i][y] = player
        scan = 1

    if x < 7 and board[x + 1][y] == opponent:
        while board[x + scan][y] == opponent and (x + scan <= 6):
            scan += 1
            currentIndex = board[x + scan][y]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x + i][y] = player
        scan = 1

    if x > 0 and y > 0 and board[x - 1][y - 1] == opponent:
        while board[x - scan][y - scan] == opponent and (x - scan >= 1 and y - scan >= 1):
            scan += 1
            currentIndex = board[x - scan][y - scan]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x - i][y - i] = player
        scan = 1

    if x > 0 and y < 7 and board[x - 1][y + 1] == opponent:
        while board[x - scan][y + scan] == opponent and (x - scan >= 1 and y + scan <= 6):
            scan += 1
            currentIndex = board[x - scan][y + scan]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x - i][y + i] = player
        scan = 1

    if x < 7 and y > 1 and board[x + 1][y - 1] == opponent:
        while board[x + scan][y - scan] == opponent and (x + scan <= 6 and y - scan >= 1):
            scan += 1
            currentIndex = board[x + scan][y - scan]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x + i][y - i] = player
        scan = 1

    if x < 7 and y < 7 and board[x + 1][y + 1] == opponent:

        while board[x + scan][y + scan] == opponent and (x + scan <= 6 and y + scan <= 6):
            scan += 1
            currentIndex = board[x + scan][y + scan]

            if currentIndex == player:
                for i in range(0, scan):
                    board[x + i][y + i] = player


# Calls AI for it's next move, pushes that move to __getMove
def getAiMove():
    validMoves = findValids(False)
    coords = AI.getMove(validMoves, game_difficulty)
    __getMove(coords[0], coords[1], False)


# Called by GUI to pass players move to __getMove, then calls the AI's move.
# PARAMS:
#     X - Column of Player's move
#     Y - Row of Player's move
def playerMove(X, Y):
    findValids(True)
    __getMove(X, Y, True)


# END playerMove


# Takes X and Y coords and the current player.
# This Function is intended for internal use only as it requires priming with other functions.
# PARAMS:
#     X - Move's X coordinate
#     Y - Move's Y coordinate
#     playerTurn - True denotes a player move (1), False denotes an AI move (2)
def __getMove(x, y, playersTurn):
    boardX = x
    boardY = y
    if playersTurn == True:
        player = 1
    else:
        player = 2
    if validMoves[boardX][boardY] == 1:
        # Flips opponent pieces as need in all 8 axis from the played piece.
        board[boardX][boardY] = player
        __flipPieces(boardX, boardY, playersTurn)
        # print("Move Complete")
    else:
        pass
        # print("Sorry, that is not a valid move.")


# END __getMove


# Takes a new board array and overwrites the current one.
# newboard must be an 2D integer array storing values in indexes 0 to 8 on both axis
#     Containing only 0, 1 or 2
def writeBoard(newBoard):
    global board
    board = newBoard
    # END writeBoard


# Used to pass the board array to other files as needed.
def getBoard():
    retArray = board
    return retArray


def getDifficulty():
    return game_difficulty


def setDifficulty(difficulty):
    global game_difficulty
    game_difficulty = difficulty
    return
