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
    if userTurn:
      player = 1
      opponent = 2
    else:
      player = 2
      opponent = 1
      
    if board[x][y] == 0 and findValidAllDirections(x, y, player, opponent):
      return True
    else:
      return False
    
#A funtion that will call checkValid for all directions - returns boolean
#Params:
# x - int - x coordinate of current place
# y - int - y coordinate of current place
# player - int - player piece value
# opponent - int - opponent piece values
def findValidAllDirections(x, y, player, opponent):
  upLeft = checkValid(x, y, -1, -1, player, opponent, getBoard(), False) # up left
  up = checkValid(x, y, 0, -1, player, opponent, getBoard(), False) # up
  upRight = checkValid(x, y, 1, -1, player, opponent, getBoard(), False) # up right
  left = checkValid(x, y, -1, 0, player, opponent, getBoard(), False) # left
  right = checkValid(x, y, 1, 0, player, opponent, getBoard(), False) # right
  downLeft = checkValid(x, y, -1, 1, player, opponent, getBoard(), False) # down left
  down = checkValid(x, y, 0, 1, player, opponent, getBoard(), False) # down
  downRight = checkValid(x, y, 1, 1, player, opponent, getBoard(), False) # down right
  return upLeft or up or upRight or left or right or downLeft or down or downRight

#A funtion to check in one direction if this position is valid - returns boolean
#Params:
# x - int - current x coordinate
# y - int - current y coordinate
# stepx - int - amount you wish to step with each depth in the x direction
# stepy - int - amount you wish to step with each depth in the y direction
# player - int - value of the player's pieces on the board
# opponent - int - value of the opponent's pieces on the board
# board - 2d list - current board state
# lastPieceOpponent - boolean - if at last recursive depth the piece was the opponent's
def checkValid(x, y, stepx, stepy, player, opponent, board, lastPieceOpponent):
  if x < 0 or x > 7 or y > 7 or y < 0:
    return False
  elif board[x][y] == opponent:
    return checkValid(x + stepx, y + stepy, stepx, stepy, player, opponent, board, True)
  elif board[x][y] == 0:
    return False
  elif not lastPiecePlayer:
    return False
  else:
    return True


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
  
  flipAllDirections(x, y, player, opponent)
  return

#A funtion that will call flipPieces for all directions - returns none
#Params:
# x - int - x coordinate of current place
# y - int - y coordinate of current place
# player - int - player piece value
# opponent - int - opponent piece values
def flipAllDirections(x, y, player, opponent):
  flipPieces(x, y, -1, -1, player, opponent, getBoard()) #up left
  flipPieces(x, y, 0, -1, player, opponent, getBoard()) # up
  flipPieces(x, y, 1, -1, player, opponent, getBoard()) # up right
  flipPieces(x, y, -1, 0, player, opponent, getBoard()) # left
  flipPieces(x, y, 1, 0, player, opponent, getBoard()) # right
  flipPieces(x, y, -1, 1, player, opponent, getBoard()) #down left
  flipPieces(x, y, 0, 1, player, opponent, getBoard()) # down
  flipPieces(x, y, 1, 1, player, opponent, getBoard()) #down right
  return

#A funtion to flip the pieces in one direction - returns none
#Params:
# x - int - current x coordinate
# y - int - current y coordinate
# stepx - int - amount you wish to step with each depth in the x direction
# stepy - int - amount you wish to step with each depth in the y direction
# player - int - value of the player's pieces on the board
# opponent - int - value of the opponent's pieces on the board
# board - 2d list - current board state
def flipPieces(x, y, stepx, stepy, player, opponent, board):
  if x < 0 or x > 7 or y > 7 or y < 0:
    return
  elif board[x][y] == opponent:
    board[x][y] = player
    return countPieces(x + stepx, y + stepy, stepx, stepy, player, opponent, board)
  else:
    return

# Calls AI for it's next move, pushes that move to __getMove
def getAiMove():
    validMoves = findValids(False)
    coords = AI.getMove(validMoves, game_difficulty)
    __getMove(coords[0], coords[1], False)
    return


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
