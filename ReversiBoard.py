
import AI 
artInt = AI.AI
#initializes the 8x8 reversi board and assigns a value of 0 to every square.
#0 = Empty square
#1 = White piece
#2 = black piece
global validMoves
global board
board = [[0 for i in range(9)] for i in range(9)]
validMoves = [[0 for i in range(9)] for i in range(9)]

#Sets the four center squares to their start of game states.  
board[4][4] = 1
board[5][5] = 1
board[4][5] = 2
board[5][4] = 2

#To be used later to take player inputs.
boardX = 1
boardY = 1


    
def main():
    print("No Code currently in main")
#Used for bugtesting
        
#END main
"""
Modifies the validMoves Array, placing a 1 in every place the defined player can legally place a move.
PARAMS:
    board - The board to be checked for valid moves. 
    Player - The player to play (1 or 0)

"""
def __findValids(player):
    
    for x in range(1, 9):
        for y in range(1, 9):
            
            if __isValid(x,y, player):
                
                validMoves[x][y] = 1
            
            else:
                
                validMoves[x][y] = 0
    printBoard(validMoves)
    retArray = validMoves[:]
    return retArray
#END _findValids
"""     
Determines if a given square is a valid move.  
PARAMS:    
    playersTurn - True when it is the human player's turn.
    x - The x position being checked
    y - The y position being checked. 

RETURN:
    Boolean, true when the direction searched finds a valid move.
"""

def __isValid(x, y, playersTurn):
    
    isValid = False
    scan = 1


    if playersTurn == True:
        player = 1
        opponent = 2
    else:
        player = 2
        opponent = 1
    
    if board[x][y] == 0:
        

        if y>=1 and board[x][y-1] == opponent:
            while board[x][y-scan] == opponent and (y-scan >= 2):
                scan += 1
                currentIndex = board[x][y-scan]
                
                if currentIndex == player:
                    isValid = True


            scan = 1
        if  y<8 and board[x][y+1] == opponent:
            while board[x][y+scan] == opponent and (y+scan <= 7): 
                scan += 1
                currentIndex = board[x][y+scan]
                
                if currentIndex == player:
                    isValid = True
                
            scan = 1       
            
        if x>1 and board[x-1][y] == opponent:
           
            while board[x-scan][y] == opponent and (x-scan >= 2):
                scan += 1
                currentIndex = board [x-scan][y]
               
                if currentIndex == player:
                    isValid = True
       
            scan = 1
        

        if  x<8 and board[x+1][y] == opponent:
           
            while board[x+scan][y] == opponent and (x+scan <= 7):
                scan += 1
                currentIndex = board[x+scan][y]
                
                if currentIndex == player:
                    isValid = True
            
            scan = 1
       
        if x>1 and y>1 and board[x-1][y-1] == opponent :
            
            while board[x-scan][y-scan] == opponent and (x-scan >= 2 and y-scan >= 2):
                scan += 1
                currentIndex = board[x-scan][y-scan]
                
                if currentIndex == player:
                    isValid = True
            
            scan = 1
            
        if  x>1 and y<8 and board[x-1][y+1] == opponent:
           
            while board[x-scan][y+scan] == opponent and (x-scan >= 2 and y+scan <= 7): 
                scan += 1
                currentIndex = board[x-scan][y+scan]
       
                if currentIndex == player:
                    isValid = True

            scan = 1
            
        if  x<8 and y>2 and board[x+1][y-1] == opponent:
         
            while board[x+scan][y-scan] == opponent and (x+scan <= 7 and y-scan >= 2):    
                scan += 1
                currentIndex = board[x+scan][y-scan]
       
                if currentIndex == player:
                    isValid = True

            scan = 1
            
        if  x<8 and y<8 and board[x+1][y+1] == opponent:

            while board[x+scan][y+scan] == opponent and (x+scan <= 7 and y+scan <= 7):  
                scan+=1
                currentIndex = board[x+scan][y+scan]
        
                if currentIndex == player:
                    isValid = True

            scan = 1
          
    return isValid                            

                                
#END __checkFlips

"""
Flips opponent's pieces to the current player's pieces.
PARAMS:
x - x coordinate of the placed piece.
y - y coordinate of the placed piece
playersTurn - Boolean, true when it is the player's Turn. 
"""
def __flipPieces(x, y, playersTurn):
    
    if playersTurn == True:
        player = 1
        opponent = 2
    else:
        player = 2
        opponent = 1
    scan = 1
    
    if y>=1 and board[x][y-1] == opponent:
        
        while board[x][y-scan] == opponent and (y-scan >= 2):
            scan += 1
            currentIndex = board[x][y-scan]
                
            if currentIndex == player:
                
                for i in range(0, scan):
                    board[x][y-i] = player
                    
        scan = 1 
 

    if  y<8 and board[x][y+1] == opponent:
        
        while board[x][y+scan] == opponent and (y+scan <= 7): 
            scan += 1
            currentIndex = board[x][y+scan]
                
            if currentIndex == player:
                
                for i in range(0, scan):
                    board[x][y+i] = player

                
        scan = 1       
            
    if x>1 and board[x-1][y] == opponent:

        while board[x-scan][y] == opponent and (x-scan >= 2): 
            scan += 1
            currentIndex = board[x-scan][y]
                
            if currentIndex == player:
                
                   for i in range(0, scan):
                    board[x-i][y] = player      

       
        scan = 1
        

    if  x<8 and board[x+1][y] == opponent:
           
        while board[x+scan][y] == opponent and (x+scan <= 7):
            scan += 1
            currentIndex = board[x+scan][y]
            
            if currentIndex == player:
                for i in range(0, scan):
                    board[x+i][y] = player

            
        scan = 1
       
    if x>1 and y>1 and board[x-1][y-1] == opponent :
           
        while board[x-scan][y-scan] == opponent and (x-scan >= 2 and y-scan >= 2):
            scan += 1
            currentIndex = board[x-scan][y-scan]
                
            if currentIndex == player:  
                for i in range(0, scan):
                    board[x-i][y-i] = player

            
        scan = 1
            
    if  x>1 and y<8 and board[x-1][y+1] == opponent:
           
        while board[x-scan][y+scan] == opponent and (x-scan >= 2 and y+scan <= 7): 
            scan += 1
            currentIndex = board[x-scan][y+scan]
       
            if currentIndex == player:
                
                for i in range(0, scan):
                    board[x-i][y+i] = player


        scan = 1
            
    if  x<8 and y>2 and board[x+1][y-1] == opponent:
         
        while board[x+scan][y-scan] == opponent and (x+scan <= 7 and y-scan >= 2):    
            scan += 1
            currentIndex = board[x+scan][y-scan]
       
            if currentIndex == player:
                
                for i in range(0, scan):
                    board[x+i][y-i] = player


        scan = 1
            
    if  x<8 and y<8 and board[x+1][y+1] == opponent:

        while board[x+scan][y+scan] == opponent and (x+scan <= 7 and y+scan <= 7):  
            scan+=1
            currentIndex = board[x+scan][y+scan]
        
            if currentIndex == player:
                
                for i in range(0, scan):
                    board[x+i][y+i] = player

        scan = 1
        
    
"""
Prints the board out in an ASCII display.
Used to aid debugging
PARAMS:
toPrint - The board to be printed
"""
def printBoard(toPrint):
    #Increments within the loop, used to print the correct board coordinate.  
    printX = 1
    printY = 1
    
    #Loops once for every row of the board. 
    for y in range(1, 9):
        
        #Prints a spaces to improve board readability.  
        print("-----------------")
        
        nextLine = "|"
        
        
        printX = 1
        
        #Loops once for every column of the board.
        for x in range(1, 9):  
            
            
            nextLine = nextLine + str(toPrint[printX][printY]) + "|"
            
            #Increments printX for use in the next run of the loop.
            printX += 1
        
        print(nextLine)
        printY += 1
    print()

#END printBoard

    
#Calls AI for it's next move, pushes that move to __getMove
def aiMove():
    
    validMoves =  __findValids(False)
    coords = artInt.easy(validMoves)
    __getMove(coords[0], coords[1], False)

#END aiMove
"""
Called by GUI to pass players move to __getMove, then calls the AI's move. 
PARAMS:
    X - Column of Player's move
    Y - Row of Player's move
"""
def playerMove(X, Y):
    validMoves =  __findValids(True)
    __getMove(X, Y, True)
    
    
    
#END playerMove
"""
Takes X and Y coords and the current player.
This Function is intended for internal use only as it requires priming with other functions.
PARAMS:
    X - Move's X coordinate
    Y - Move's Y coordinate
    playerTurn - True denotes a player move (1), False denotes an AI move (2)
"""
def __getMove( X, Y, playersTurn):
    
    printBoard(board)
    boardX = X
    boardY = Y
    if playersTurn == True:
        Player = 1
    else:
        Player = 2

    if (validMoves[boardX][boardY] == 1):
            
        #Flips opponent pieces as need in all 8 axis from the played piece. 
                                    
        board[boardX][boardY] = Player
        __flipPieces(boardX, boardY, playersTurn)
        print("Move Complete")
        
        

    else:
        
        print("Sorry, that is not a valid move.")
        

#END __getMove

"""
Takes a new board array and overwrites the current one.
newboard must be an 2D integer array storing values in indexes 0 to 8 on both axis
    Containing only 0, 1 or 2
""" 
def writeboard (newBoard):
    global board
    board = newBoard
 #END Writeboard

"""
Used to pass the board array to other files as needed.
"""
def getBoard():
    retArray = board[:]
    return retArray;
#END getboard

if __name__ == "__main__":
    main()
    print(board[boardX][boardY])