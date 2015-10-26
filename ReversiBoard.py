


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

#printer = GUI()

#To be used later to take player inputs.
boardX = 1
boardY = 1


    
def main():
    playerOne = True;
    
    while True:
        
        getMove(0, 0, playerOne)
        playerOne = not playerOne
        

def findValids(board, Player):
    
    for x in range(1, 9):
        for y in range(1, 9):
            
            if (checkFlips(1, 0, x, y, Player, True) or 
            checkFlips(0, 1, x, y, Player, True) or 
            checkFlips(-1, 0, x, y, Player, True) or 
            checkFlips(0, -1, x, y, Player, True) or 
            checkFlips(1, 1, x, y, Player, True ) or 
            checkFlips(-1, -1, x, y, Player, True) or 
            checkFlips(-1, 1, x, y, Player, True) or 
            checkFlips(1, -1, x, y, Player, True)):
                
                validMoves[x][y] = 1
            
            else:
                
                validMoves[x][y] = 0
    printBoard(validMoves)
    return validMoves
        
#Finds and flips appropriate opponent in a direction of travel defined by dirX and dirY
    #Example: when dirX = 0 and dirY = -1 the squares directly below the new piece are checked. 

def checkFlips(dirX, dirY, X, Y, Player, ifReturn):
    
    if Player == True:
        checkpieces = 1
    else:
        checkpieces = 2
        
        
    scanX = 0
    scanY = 0
    
    boardX = X
    boardY = Y
   
    while(1<(boardX+scanX)<8 and 1<(boardY+scanY)<8):
                
                
                
                scanX = scanX + 1
                scanY = scanY + 1
                #Print statements used for debugging.

                if (board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] == 0):
                    
                    break;
                
                elif (scanX == 1 and scanY == 1 and board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] == checkpieces):
                    
                    break;
 
                elif( board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] ==checkpieces and (scanX>1 or scanY>1)):
                    print("x: " + str(boardX+(scanX*dirX)))
                    print("y: " + str(boardY+(scanY*dirY)))
                    print(dirX, dirY)
                    
                    if ifReturn:

                        return True

                    else:
                        while scanX>=1 or scanY>=1:
                        
                            board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] = checkpieces
                        
                            
                        
                            scanX = scanX - 1
                            scanY = scanY - 1
   
                    break
   
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

    

    

def getMove( X, Y, turn):
    
    printBoard(board)
    
    if turn == True:
        Player = 1
    else:
        Player = 2
    validMoves =  findValids(board, turn)
    #Loops the program until a valid move takes place.
    while True:
    
   
        #Loops the program until a valid Y coordinate is given.     
        while True:
            
            boardX = int(input("In which column would you like to play? "))
            
            if(0>boardX>7):
        
                print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    
            else:
            
                break

        #Loops the program until a valid Y coordinate is given.     
        while True:
    
            
            boardY = int(input("In which row would you like to play? "))

            
            if(1>boardY>8):
        
                
                print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    
            else:
            
                break


        
    
        if (validMoves[boardX][boardY] == 1):
            
            #Flips opponent pieces as need in all 8 axis from the played piece. 
            checkFlips(1, 0, boardX, boardY, Player, False)
            checkFlips(0, 1, boardX, boardY, Player, False)
            checkFlips(-1, 0, boardX, boardY, Player, False)
            checkFlips(0, -1, boardX, boardY, Player, False)
            checkFlips(1, 1, boardX, boardY, Player, False)
            checkFlips(-1, -1, boardX, boardY, Player, False)
            checkFlips(-1, 1, boardX, boardY, Player, False)
            checkFlips(1, -1, boardX, boardY, Player, False)
                                    
            board[boardX][boardY] = Player
            print("Move Complete")
            turn = turn+1
            #GUI.updateboardpieces(board)
            break

        else:
        
            print("Sorry, that is not a valid move.")
        

#END GetMove

#Takes a new board array and overwrites the current one.
#newboard must be an 2D integer array storing values in indexes 0 to 8 on both axis. 
def writeboard (newBoard):
    
        board = newBoard
        



if __name__ == "__main__":
    main()
    print(board[boardX][boardY])