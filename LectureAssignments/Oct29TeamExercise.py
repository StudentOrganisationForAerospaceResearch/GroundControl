"""
2015/10/29

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
Takes a string input and then repeats it the number of times the user specifies as well as splices it if necessary
"""


# Function that takes an input string & repeats it the amount of times the user wants (splices if asked to)
# PARAMS:
#   inputString = User's inputted string
#   timesToMultiply = Times to repeat the string (or spliced string)
#   startIndex = OPTIONAL - The start index from which to start splicing the string
#   endIndex = OPTIONAL - The end index from which to stop splicing the string
def mult(inputString, timesToMultiply, startIndex = 0, endIndex = -1):
    # Checks to set the endIndex to include the whole string if the user does not specify one
    if endIndex == -1:
        endIndex = len(inputString)

    # Splices the string & repeats it and then returns it back
    splicedString = inputString[startIndex:endIndex]
    return splicedString * timesToMultiply


# Function that takes the same inputs as mult however mentions what is being tested & whether it passed the test or failed
# PARAMS:
#   expected = Expected return of the function
#   param1 = User's inputted string
#   param2 = Times to repeat the string (or spliced string)
#   param3 = OPTIONAL - The start index from which to start splicing the string
#   param4 = OPTIONAL - The end index from which to stop splicing the string
def tester(expected, param1, param2, param3 = None, param4 = None):
    print("\nTesting '" + str(param1) + "' by repeating it " + str(param2) + " times & start index being " + str(param3) + " & end index being " + str(param4) + ". (Expected = '" + expected + "')")

    # Stores & prints out the final string
    multResponse = mult(param1, param2, param3, param4)
    print("'" + multResponse + "'")

    # Tells whether or not the test passed
    if multResponse == expected:
        print("PASSED")
    else:
        print("FAILED")


# Main function to call and test the "mult" function
def main():
    tester("eee", "Test", 3, 1, 2)
    tester("estestest", "Test", 3, 1)
    tester("TestTestTest", "Test", 3)
    tester("", "Nathan", 3, 3, 3)
    tester("", "Nathan", 3, 3, 2)


# Calls the main function if the file is called directly
if __name__ == '__main__':
    main()
