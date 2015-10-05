"""
2015/10/01

Group 22, CPSC 231

Murray Cobbe Nathan Meulenbroek Sharjeel Junaid

Description: A game that asks the player for 10 numbers and sees if they can guess the computer's number
"""
import random


def main():
    targetNumber = random.randrange(1, 101)
    introText()
    for n in range(10):
        guess = getInput(n)

        check(guess, targetNumber)

    endGame(targetNumber)


# Prints intro text and holds for player start command.
def introText():
    print(
        """
          Welcome to 10 questions!
          
          The Computer has already selected a number.
          This number is between 1 and 100.
          You will have 10 attempts to guess this number.
          After each guess you will be told if your guess is larger or smaller than the computer's numbers.
          
          Press enter when you are ready to begin.""")
    input()


# Takes input from the player
def getInput(n):
    guess = int(input("Please enter guess number " + str(n + 1) + ": "))
    return (guess)


# After the player is out of guesses, asks them for a final answer.
def endGame(targetNumber):
    print("The game is over. ")
    guess = int(input("What do you think the computer's number is?"))
    if check(guess, targetNumber) == True:
        print("Congratulations you win")
    else:
        print("Sorry, you lose.")
    # Checks the user input against the computer's guess.


def check(guess, targetNumber):
    if guess == targetNumber:
        print("Your guess is equal! Use this at the end of the program\n")
        return True
    if guess > targetNumber:
        print("Your guess was high, try lower!\n")

    if guess < targetNumber:
        print("Your guess was low, try higher!\n")


main()
