""" 
2self.BOARDEDGELOW15/12/self.BOARDEDGELOWself.BOARDEDGEHIGH

Group 22, CPSC 2self.BOARDEDGEHIGH1

Murray Cobbe Nathan Meulenbroek Sharjeel Junaid

Description: 
Excercise code that simualtes a Tic Tac Toe board. 
"""



#Class for the State of the Tic Tac Toe game.
#PARAMS:
#    playerToken - token to be used to mark player moves.
#    aiToken - token to be used to mark the AI moves.
class TicTacToeState:

    def __init__(self, playerToken, aiToken):
        self.player = playerToken.upper()
        self.ai = aiToken.upper()
        self.BLANKSPACES= "b"
        self.BOARDEDGEHIGH  = 3  
        self.BOARDEDGELOW = 0
        self.board = [[self.BLANKSPACES for i in range(self.BOARDEDGEHIGH)] for i in range(self.BOARDEDGEHIGH)]

#Function plays a player piece at specificed coordinates, does nothing if the move is invalid
#PARAMS
#    row - the row in which the piece is to be played
#    column - the column in which the piece is to be played
    def playerMove(self, row, column):
        if row>=self.BOARDEDGELOW and row<self.BOARDEDGEHIGH and column>=self.BOARDEDGELOW and column<self.BOARDEDGEHIGH and self.board[row][column] == self.BLANKSPACES:
            self.board[row][column] = self.player
#Function plays a player piece at specificed coordinates, does nothing if the move is invalid
#PARAMS
#    row - the row in which the piece is to be played
#    column - the column in which the piece is to be played    
    def aiMove(self, row, column):
        if row>=self.BOARDEDGELOW and row<self.BOARDEDGEHIGH and column>=self.BOARDEDGELOW and column<self.BOARDEDGEHIGH and self.board[row][column] == self.BLANKSPACES:
            self.board[row][column] = self.ai
#Function returns true iff the boards of this object and the passed object are identical.
#PARAMS:
#    otherGame - another TicTacToeState object.
    def isSame(self, otherGame):
        same = False
        if self.board == otherGame.board:
            same = True
        return same
#Test code.      
if __name__ == "__main__":
    tic = TicTacToeState("x", "o")
    tac = TicTacToeState("X", "o")
    print(tic.isSame(tac))
    tic.playerMove(0, 1)
    tac.aiMove(0,1)
    print(tic.isSame(tac)) 
    
    #Returns false because tic and tac are different objects. As in they're different instances of the same 
    #class, but each instance starts up new variables. It does not maintain any of the same references. 
    
    print(tic.board)
    print(tac.board)
       

        
    