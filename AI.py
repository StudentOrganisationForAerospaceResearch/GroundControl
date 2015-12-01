from ReversiBoard import getBoard

#assign board places static values based on their strategic value. Differs by level of difficulty
STATICBOARDVALUESEASY = [[100,50,50,50,50,50,50,100],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[100,50,50,50,50,50,50,100]]
STATICBOARDVALUESMEDIUM = [[100,50,50,50,50,50,50,100],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[100,50,50,50,50,50,50,100]]
STATICBOARDVALUESHARD = [[99,-8,8,6,6,8,-8,99],[-8,-24,-4,-3,-3,-4,-24,-8],[8,-4,7,4,4,7,-4,8],[6,-3,4,0,0,4,-3,6],[6,-3,4,0,0,4,-3,6],[8,-4,7,4,4,7,-4,8],[-8,-24,-4,-3,-3,-4,-24,-8],[99,-8,8,6,6,8,-8,99]]

class AI():
    
    #Function that will return a move from the AI. Returns only the coordinates, does not play the piece itself
    #PARAMS:
    #        validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates. Does not matter the size of the board
    def getMove(validMoves, level):
        if level == 1:
            return self.easy(validMoves)
        elif level == 2:
            return self.medium(validMoves)
        elif level == 3:
            return self.hard(validMoves)
        
    def easy(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and STATICBOARDVALUESEASY[x][y] > value:
                    coords = [x,y]
        
        return coords
        
    def medium(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and STATICBOARDVALUESMEDIUM[x][y] > value:
                    coords = [x,y]
        
        return coords
        
    def hard(validMoves):
        dynamicBoard = [[0 for i in range(8)] for i in range(8)]
        finalBoard = [[0 for i in range(8)] for i in range(8)]
        coords = [0,0]
        value = 0
        
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                dynamicBoard[x][y] = countAllDirections(x, y)
                
        #create final board by adding static board values with how many pieces that move would flip
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                finalBoard[x][y] = STATICBOARDVALUESHARD[x][y] + dynamicBoard[x][y]
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(finalBoard)):
            for y in range(len(finalBoard[1])):
                if finalBoard[x][y] == 1 and STATICBOARDVALUESHARD[x-1][y-1] > value:
                    coords = [x,y]
        
        return coords
        
    def countAllDirections(x, y):
      upLeft = countPieces(x, y, -1, -1, getBoard())
      up = countPieces(x, y, 0, -1, getBoard())
      upRight = countPieces(x, y, 1, -1, getBoard())
      left = countPieces(x, y, -1, 0, getBoard())
      right = countPieces(x, y, 1, 0, getBoard())
      downLeft = countPieces(x, y, -1, 1, getBoard())
      down = countPieces(x, y, 0, 1, getBoard())
      downRight = countPieces(x, y, 1, 1, getBoard())
    
    return up + upLeft + upRight + right + left + downLeft + down + downRight
        
    def countPieces(x, y, stepx, stepy, board):
        if x < 0 or x > 7 or y > 7 or y < 0:
            return 0
        elif board[x][y] == 2:
            return countPieces(x + stepx, y + stepy, stepx, stepy, board) + 1
        else:
            return 0
        