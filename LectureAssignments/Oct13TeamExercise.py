"""
2015/10/13

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description: Program that takes the average of several GPAs
***Assumes smart user***
Known errors:
-buffer limit can be exceeded if too many values entered
-does not check for null input error
-does not validate that input is numerical

"""

# Function to take the user's inputted grade and validates whether or not it is within bounds and return's the result - returns boolean
# Params:
#    inputGrade - The grade as a GPA as a floating point
def validInput(inputGrade):
    if (inputGrade <= 4.3 and inputGrade >= 0.0):
        return True
    else:
        print(inputGrade, "is invalid! Please input another value")
        return False


# Main function to prompt user for input and display average
def main():
    keepGoing = True
    sumOfGrades = 0.0
    numberOfGradesEntered = 0

    # Print program description
    print("This is a program that will take the average of all the grades entered. \n" +
          "Please only enter grades in between the values 0 and 4.3, inclusive. \n" +
          "Enter '-1' to finish program and display average")

    # Flag tripped when input == -1, then displays average
    # Validating input in if statement, displays error message in function
    # Keeps count of num of grades entered and the sum until flag is entered
    while (keepGoing == True):
        userInput = float(input("Please Enter Grade: "))
        if (userInput == -1):
            keepGoing = False
            print("The Average Of The Grades Entered Is:", (sumOfGrades / numberOfGradesEntered))
        elif validInput(userInput):
            sumOfGrades += userInput
            numberOfGradesEntered += 1


# Calls the main method if the file is called directly
if __name__ == '__main__':
    main()
