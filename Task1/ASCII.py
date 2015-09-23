print("Welcome to" + "\n" + 
"""╦═╗┌─┐┬  ┬┌─┐┬─┐┌─┐┬
╠╦╝├┤ └┐┌┘├┤ ├┬┘└─┐│
╩╚═└─┘ └┘ └─┘┴└─└─┘┴""" + "\n" + 
"In this game you will be able to..." + "\n" +
"""╔╦╗┬ ┬┌─┐┌─┐  ╔═╗┌─┐┌┬┐┌─┐┌┬┐┬ ┬┬┌┐┌┌─┐  
 ║ └┬┘├─┘├┤   ╚═╗│ ││││├┤  │ ├─┤│││││ ┬  
 ╩  ┴ ┴  └─┘  ╚═╝└─┘┴ ┴└─┘ ┴ ┴ ┴┴┘└┘└─┘ 
"""+ "\n" +
"You will eventually be able to click on the tile where you want to play your piece, but for now, please input coordinates. The point of the game is as follows:"+ "\n" +
"""╔═╗┌─┐┌┬┐  ┌─┐┌─┐  ┌┬┐┌─┐┌┐┌┬ ┬  ┌─┐┬┌─┐┌─┐┌─┐┌─┐
║ ╦├┤  │   ├─┤└─┐  │││├─┤│││└┬┘  ├─┘│├┤ │  ├┤ └─┐
╚═╝└─┘ ┴   ┴ ┴└─┘  ┴ ┴┴ ┴┘└┘ ┴   ┴  ┴└─┘└─┘└─┘└─┘
┌─┐┌─┐  ┌─┐┌─┐┌─┐┌─┐┬┌┐ ┬  ┌─┐                   
├─┤└─┐  ├─┘│ │└─┐└─┐│├┴┐│  ├┤                    
┴ ┴└─┘  ┴  └─┘└─┘└─┘┴└─┘┴─┘└─┘                   
┬┌┐┌  ┬ ┬┌─┐┬ ┬┬─┐  ┌─┐┌─┐┬  ┌─┐┬ ┬┬─┐           
││││  └┬┘│ ││ │├┬┘  │  │ ││  │ ││ │├┬┘           
┴┘└┘   ┴ └─┘└─┘┴└─  └─┘└─┘┴─┘└─┘└─┘┴└─  
""")
#Ensures the Program does not continue until it has a good value for X.
while True:
    
    #Prompts the user for an X coordinate
    boardX = int(input("In which column would you like to play? "))

    #Checks the user input for validity.
    if(boardX>=8):
        
        #Prompts the user for a different input if their move in invalid.
        print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    
    else:
        #if the users input is valid, continues the program. 
        break

#Ensures the Program does not continue until it has a good value for X.    
while True:
    
    #Prompts the user for a Y coordinate
    boardY = int(input("In which row would you like to play? "))

    #Checks the user input for validity.
    if(boardY>=8):
        
        #Prompts the user for a different input if their move in invalid.
        print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    
    else:
        #if the users input is valid, continues the program. 
        break

#formats and prints the players requested move.
print("Your piece will be played on square at X: " + str(boardX) + " Y: "  + str(boardY))

