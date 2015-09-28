

#initializes the 8x8 reversi board and assigns a value of 0 to every square.
#0 = Empty square
#1 = White piece
#2 = black piece
board = [[0 for i in range(8)] for i in range(8)]

#Sets the four center squares to their start of game states.  
board[3][3] = 1
board[4][4] = 1
board[3][4] = 2
board[4][3] = 2

turn = 1

#To be used later to take player inputs.
boardX = 0
boardY = 0


#Finds and flips appropriate opponent in a direction of travel defined by dirX and dirY
    #Example: when dirX = 0 and dirY = -1 the squares directly below the new piece are checked. 
def checkFlips(dirX, dirY):
    
    scanX = 0
    scanY = 0
   
    while(-1<(boardX+scanX)<8 and -1<(boardY+scanY)<8):
                
                
                
                scanX = scanX + 1
                scanY = scanY + 1
                if (board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] == 0 ):
                    
                    break;
 
                elif( board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] ==Player and (scanX>1 or scanY>1)):
                    
                    print(dirX, dirY)
                    while scanX>=1 or scanY>=1:
                        
                        board[boardX+(scanX*dirX)][boardY+(scanY*dirY)] = Player
                        scanX = scanX - 1
                        scanY = scanY - 1
   
                    break




   
def printBoard():
    #Increments within the loop, used to print the correct board coordinate.  
    printX = 0
    printY = 0
    
    #Loops once for every row of the board. 
    for y in range(8):
        
        #Prints a spaces to improve board readability.  
        print("-----------------")
        
        nextLine = "|"
        
        
        printX = 0
        
        #Loops once for every column of the board.
        for x in range(8):  
            
            
            nextLine = nextLine + str(board[printX][printY]) + "|"
            
            #Increments printX for use in the next run of the loop.
            printX = printX+1
        
        print(nextLine)
        printY = printY+1

#END printBoard

    


while True:
#START getMove
    printBoard()
    
    Player = (turn%2)+1
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

            
            if(0>boardY>7):
        
                
                print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    
            else:
            
                break


        
    
        if (board[boardX][boardY] == 0):
            
            #Flips opponent pieces as need in all 8 axis from the played piece. 
            checkFlips(1, 0)
            checkFlips(0, 1)
            checkFlips(-1, 0)
            checkFlips(0, -1)
            checkFlips(1, 1)
            checkFlips(-1, -1)
            checkFlips(-1, 1)
            checkFlips(1, -1)
                                    
            board[boardX][boardY] = Player
            print("Move Complete")
            turn = turn+1
            
            break

        else:
        
            print("Sorry, that is not a valid move.")
        


#END GetMove



print(board[boardX][boardY])