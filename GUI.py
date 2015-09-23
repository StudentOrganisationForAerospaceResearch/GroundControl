"""
2015/09/23

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
The Program Will Print Out The Reversi Table Using Turtle Graphics & Prompt The User For An Input Piece Coordinate & Echo It Back Out
"""

# Imports In Module(s) That Will Be Utilized
import turtle

# Initialize Variables
boardTopLeftX = -250.0
boardTopLeftY = 250.0
placePieceX = 0.0
placePieceY = 0.0
moveCounter = 1

# Initialize Board 8x8 Matrix
boardMatrix = [[0 for boardMatrixIndex in range(9)] for boardMatrixIndex in range(9)]

# Initialize The Display Out & The First Turtle
displayOut = turtle.Screen()
turtle1 = turtle.Turtle()

# Hides The Turtle Pointer
turtle1.hideturtle()

# Sets The Drawing Speed Of The Turtle
turtle1.speed(10)

# For Loop To Teleport The Turtle To Coordinates & Print The Reversi Table
for indexCounter in range(9):
    # Lifts Up The Turtle & Prevents It From Leaving A Trail
    turtle1.up()
    # Teleports The Turtle To The Left Hand Side Of The Next Row
    turtle1.goto(boardTopLeftX, boardTopLeftY - indexCounter * boardTopLeftY / 4)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()
    # Prints Out The Row's Line
    turtle1.forward(boardTopLeftX * -2)

    # Turns The Turtle Right To Print Out A Vertical Line
    turtle1.right(90)
    # Lifts Up The Turtle & Prevents It From Leaving A Trail
    turtle1.up()
    # Teleports The Turtle To The Top Of The Next Column
    turtle1.goto(boardTopLeftX - indexCounter * boardTopLeftX / 4, boardTopLeftY)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()
    # Prints Out The Row's Line
    turtle1.forward(boardTopLeftY * 2)
    # Turns The Turtle Back Left To Print Out The Horizontal Line
    turtle1.left(90)

# Welcomes The User To The Program
print("Welcome to" + "\n" +
      """???????  ???????????
      ????? ?????? ???????
      ?????? ?? ??????????""" + "\n" +
      "In this game you will be able to..." + "\n" +
      """???? ???????  ???????????????? ????????
       ? ????????   ???? ??????  ? ???????? ?
       ?  ? ?  ???  ??????? ???? ? ? ????????
      """+ "\n" +
      "You will eventually be able to click on the tile where you want to play your piece, but for now, please input coordinates. The point of the game is as follows:"+ "\n" +
      """?????????  ??????  ?????????? ?  ????????????????
      ? ???  ?   ??????  ????????????  ?????? ?  ?? ???
      ?????? ?   ? ????  ? ?? ???? ?   ?  ?????????????
      ??????  ??????????????? ?  ???
      ??????  ???? ????????????  ??
      ? ????  ?  ???????????????????
      ????  ? ????? ????  ???????  ???? ????
      ????  ???? ?? ????  ?  ? ??  ? ?? ????
      ????   ? ?????????  ??????????????????
      """)

# Endless While Loop To Handle The User's Inputted Move
while True:
    # Prompts The User For Their Move's Location & Stores It In Variables
    placePieceX = int(input("\nRow You Would Like To Place A Piece In: "))
    placePieceY = int(input("Column You Would Like To Place A Piece In: "))

    # Lifts Up The Turtle & Prevents It From Leaving A Trail
    turtle1.up()
    # Teleports To The Relevant Tile
    turtle1.goto(boardTopLeftX - (placePieceX - 0.5) * boardTopLeftX / 4, boardTopLeftY - placePieceY * boardTopLeftY / 4)
    # Lowers The Turtle & Allows It To Leave A Trail Again
    turtle1.down()
    # Starts The Fill Command (To Fill In The Printed Circle)
    turtle1.begin_fill()

    # Checks To See Whether Or Not The Coordinates The User Entered Are Within Bounds
    if placePieceX <= 8 and placePieceY <= 8 and placePieceX >= 1 and placePieceY >= 1:
        # Checks To See Whether Or Not The Entry Index In The Matrix Is Free
        if boardMatrix[placePieceX][placePieceY] == 0:
            # If / Else Statement To Check Which Colour To Fill The Circle With (Odd Is Blue & Even Is Red) & It Also Stores Who Occupied The Tile
            if moveCounter %2 == 0:
                # If The Number Is Even, Fills It Blue & Stores That They Occupied It
                turtle1.fillcolor("Red")
                boardMatrix[placePieceX][placePieceY] = "Red"
                moveCounter += 1
            else:
                # If The Number Is Odd, Fills It Red & Stores That They Occupied It
                turtle1.fillcolor("Blue")
                boardMatrix[placePieceX][placePieceY] = "Blue"
                moveCounter += 1

            # Prints Out A Circle In The Tile
            turtle1.circle(-boardTopLeftX / 8)
            # Ends The Fill Command
            turtle1.end_fill()
        else:
            # Informs The User That Their Entered Move Coordinates Were Invalid
            print("Invalid Move!")
    else:
        # Informs The User That Their Entered Move Coordinates Were Invalid
        print("Invalid Move!")

# Closes The Program If The GUI Overlay Is Clicked
displayOut.exitonclick()
