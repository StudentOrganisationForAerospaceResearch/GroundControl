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

#Contunuous loop until input validated
while True:
    boardX = int(input("In which column would you like to play? "))

    #If position outside bounds, continue. Else, break
    if(boardX>=8 or boardX<0):
        print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    else:
        break

#Continues loop until input validated   
while True:
    boardY = int(input("In which row would you like to play? "))

    #Checks to see if input is within bounds. If invalid, continue, else, break
    if(boardY>=8 or boardY<0):
        print("Sorry, that is not a valid board position. Please use a number between 0 and 7.")
    else:
        break

#Format and print move requested
print("Your piece will be played on square at X: " + str(boardX) + " Y: "  + str(boardY))
