"""
2015/12/08

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This part of the game is in charge of handling the calls from the backend for AI responses
"""
class AI:
    # Assign board places static values based on their strategic value. Differs by level of difficulty
    STATICBOARDVALUESEASY = [[100, 50, 50, 50, 50, 50, 50, 100], [50, 10, 10, 10, 10, 10, 10, 50],
                             [50, 10, 10, 10, 10, 10, 10, 50], [50, 10, 10, 10, 10, 10, 10, 50],
                             [50, 10, 10, 10, 10, 10, 10, 50], [50, 10, 10, 10, 10, 10, 10, 50],
                             [50, 10, 10, 10, 10, 10, 10, 50], [100, 50, 50, 50, 50, 50, 50, 100]]
    STATICBOARDVALUESMEDIUM = [[100, 50, 50, 50, 50, 50, 50, 100], [50, 5, 15, 10, 10, 15, 5, 50],
                               [50, 5, 15, 10, 10, 15, 5, 50], [50, 5, 15, 10, 10, 15, 5, 50],
                               [50, 5, 15, 10, 10, 15, 5, 50], [50, 5, 15, 10, 10, 15, 5, 50],
                               [50, 5, 15, 10, 10, 15, 5, 50], [100, 50, 50, 50, 50, 50, 50, 100]]
    STATICBOARDVALUESHARD = [[99, -8, 8, 6, 6, 8, -8, 99], [-8, -24, -4, -3, -3, -4, -24, -8],
                             [8, -4, 7, 4, 4, 7, -4, 8], [6, -3, 4, 0, 0, 4, -3, 6], [6, -3, 4, 0, 0, 4, -3, 6],
                             [8, -4, 7, 4, 4, 7, -4, 8], [-8, -24, -4, -3, -3, -4, -24, -8],
                             [99, -8, 8, 6, 6, 8, -8, 99]]

    # Function that will return a move from the AI Returns only the coordinates, does not play the piece itself
    # PARAMS:
    #       validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates.
    #        Does not matter the size of the board
    #       level - int - desired level of play
    def getMove(validMoves, level, board):
        if level == 1:
            return AI.easy(validMoves)
        elif level == 2:
            return AI.medium(validMoves)
        elif level == 3:
            return AI.aggressive(validMoves, board)
        elif level == 4:
            return AI.extreme(validMoves)

    # Function to return move of easy AI
    # PARAMS:
    #       validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates.
    #        Does not matter the size of the board
    def easy(validMoves):
        coords = [0, 0]
        value = 0

        # Loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and AI.STATICBOARDVALUESEASY[x][y] > value:
                    coords = [x, y]

        return coords

    # Function to return move of medium AI
    # PARAMS:
    #       validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates.
    #        Does not matter the size of the board
    def medium(validMoves):
        coords = [0, 0]
        value = 0

        # Loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and AI.STATICBOARDVALUESMEDIUM[x][y] > value:
                    coords = [x, y]

        return coords

    # Function to return move of extreme AI
    # PARAMS:
    #       validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates.
    #        Does not matter the size of the board
    def extreme(validMoves):
        coords = [0, 0]
        value = 0

        # Loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and AI.STATICBOARDVALUESHARD[x][y] > value:
                    coords = [x, y]

        return coords

    # Function to return move of aggressive AI Is recursively checking in all directions to find how many pieces the
    #  board will flip.
    # PARAMS:
    #       validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates.
    #        Does not matter the size of the board
    def aggressive(validMoves, board):
        dynamicBoard = [[0 for i in range(8)] for i in range(8)]
        finalBoard = [[0 for i in range(8)] for i in range(8)]
        coords = [0, 0]
        value = 0

        # Dynamically generate board values for how many pieces each spot will flip
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                dynamicBoard[x][y] = AI.countAllDirections(x, y, board)

        # Create final board by adding static board values with how many pieces that move would flip
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                finalBoard[x][y] = AI.STATICBOARDVALUESHARD[x][y] + dynamicBoard[x][y]

        # Loop through valid moves board looking for most strategic available location
        for x in range(len(finalBoard)):
            for y in range(len(finalBoard[1])):
                if validMoves[x][y] == 1 and finalBoard[x - 1][y - 1] > value:
                    coords = [x, y]

        return coords

    # A function that counts in all the possible directions away from a piece recursively
    # PARAMS:
    #       x - int - x coordinate
    #       y - int - y coordinate
    def countAllDirections(x, y, board):
        upLeft = AI.countPieces(x, y, -1, -1, board)
        up = AI.countPieces(x, y, 0, -1,  board)
        upRight = AI.countPieces(x, y, 1, -1,  board)
        left = AI.countPieces(x, y, -1, 0,  board)
        right = AI.countPieces(x, y, 1, 0,  board)
        downLeft = AI.countPieces(x, y, -1, 1,  board)
        down = AI.countPieces(x, y, 0, 1,  board)
        downRight = AI.countPieces(x, y, 1, 1,  board)

        return up + upLeft + upRight + right + left + downLeft + down + downRight

    # A function that counts in one direction and returns how many pieces it flips
    # PARAMS:
    #       x - int - x coordinate
    #       y - int - y coordinate
    #       stepX - int - step in x direction
    #       stepY - int - step in y direction
    #       board - 2D list of current board state
    def countPieces(x, y, stepX, stepY, board):
        if x < 0 or x > 7 or y > 7 or y < 0:
            return 0
        elif board[x][y] == 2:
            # If board piece is player's, increment and look at the next piece
            return 1 + AI.countPieces(x + stepX, y + stepY, stepX, stepY, board)
        else:
            return 0
