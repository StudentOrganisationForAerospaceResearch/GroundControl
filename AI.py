import ReversiBoard

class AI():
    #assign board places static values based on their strategic value. Differs by level of difficulty
    STATICBOARDVALUESEASY = [[100,50,50,50,50,50,50,100],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[50,10,10,10,10,10,10,50],[100,50,50,50,50,50,50,100]]
    STATICBOARDVALUESMEDIUM = [[100,50,50,50,50,50,50,100],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[50,5,15,10,10,15,5,50],[100,50,50,50,50,50,50,100]]
    STATICBOARDVALUESHARD = [[99,-8,8,6,6,8,-8,99],[-8,-24,-4,-3,-3,-4,-24,-8],[8,-4,7,4,4,7,-4,8],[6,-3,4,0,0,4,-3,6],[6,-3,4,0,0,4,-3,6],[8,-4,7,4,4,7,-4,8],[-8,-24,-4,-3,-3,-4,-24,-8],[99,-8,8,6,6,8,-8,99]]
    
    #Function that will return a move from the AI. Returns only the coordinates, does not play the piece itself
    #PARAMS:
    #        validMoves - 2D array that contains all the valid moves on the board as a 1 in the specific coordinates. Does not matter the size of the board
    def getMove(validMoves, level):
        if level == 1:
            return AI.easy(validMoves)
        elif level == 2:
            return AI.medium(validMoves)
        elif level == 3:
            return AI.agressive(validMoves)
        elif level == 4:
            return AI.extreme(validMoves)
        
    def easy(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and AI.STATICBOARDVALUESEASY[x][y] > value:
                    coords = [x,y]
        
        return coords
        
    def medium(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and AI.STATICBOARDVALUESMEDIUM[x][y] > value:
                    coords = [x,y]
        
        return coords

    def medium(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and AI.STATICBOARDVALUESHARD[x][y] > value:
                    coords = [x,y]
        
        return coords
        
    def agressive(validMoves):
        dynamicBoard = [[0 for i in range(8)] for i in range(8)]
        finalBoard = [[0 for i in range(8)] for i in range(8)]
        coords = [0,0]
        value = 0
        
        #dynamically generate board values for how many pieces each spot will flip
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                dynamicBoard[x][y] = AI.countAllDirections(x, y)
                
        #create final board by adding static board values with how many pieces that move would flip
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                finalBoard[x][y] = AI.STATICBOARDVALUESHARD[x][y] + dynamicBoard[x][y]
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(finalBoard)):
            for y in range(len(finalBoard[1])):
                if validMoves[x][y] == 1 and finalBoard[x-1][y-1] > value:
                    coords = [x,y]
        
        return coords
        
    def countAllDirections(x, y):
      upLeft = AI.countPieces(x, y, -1, -1, ReversiBoard.getBoard())
      up = AI.countPieces(x, y, 0, -1, ReversiBoard.getBoard())
      upRight = AI.countPieces(x, y, 1, -1, ReversiBoard.getBoard())
      left = AI.countPieces(x, y, -1, 0, ReversiBoard.getBoard())
      right = AI.countPieces(x, y, 1, 0, ReversiBoard.getBoard())
      downLeft = AI.countPieces(x, y, -1, 1, ReversiBoard.getBoard())
      down = AI.countPieces(x, y, 0, 1, ReversiBoard.getBoard())
      downRight = AI.countPieces(x, y, 1, 1, ReversiBoard.getBoard())
    
      return up + upLeft + upRight + right + left + downLeft + down + downRight
        
    def countPieces(x, y, stepx, stepy, board):
        if x < 0 or x > 7 or y > 7 or y < 0:
            return 0
        elif board[x][y] == 2:
            return AI.countPieces(x + stepx, y + stepy, stepx, stepy, board) + 1
        else:
            return 0
        
