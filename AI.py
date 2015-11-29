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
            return AI.easy(validMoves)
        elif level == 2:
            return AI.medium(validMoves)
        elif level == 3:
            return AI.hard(validMoves)
        
    def easy(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and STATICBOARDVALUESEASY[x-1][y-1] > value:
                    coords = [x,y]
        
        return coords
        
    def medium(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and STATICBOARDVALUESMEDIUM[x-1][y-1] > value:
                    coords = [x,y]
        
        return coords
        
    def hard(validMoves):
        coords = [0,0]
        value = 0
        
        #loop through valid moves board looking for most strategic available location
        for x in range(len(validMoves)):
            for y in range(len(validMoves[1])):
                if validMoves[x][y] == 1 and STATICBOARDVALUESHARD[x-1][y-1] > value:
                    coords = [x,y]
        
        return coords
        
    def iterateOverPieces():
        return
        