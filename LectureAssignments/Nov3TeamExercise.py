"""
2015/10/27

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description: Includes a function to drop the smallest value from the provided list
"""


# Function that takes a list of numbers and deletes the smallest value - returns list
# PARAMS:
#   numList - list of numbers
def dropMin(numList):
    if len(numList) != 0:
        index = 0
        minimum = numList[0]
        pos = 0

        # iterate through list and find and store smallest value
        while index < len(numList):
            if numList[index] < minimum:
                pos = index
            index += 1

        # delete smallest number
        del numList[pos]

    return numList


# Function that takes the same inputs as dropMin, however mentions what is being tested & whether it passed the test or failed
# PARAMS:
#   expected - expected list
#   param1 - list of numbers that will be passed on
def tester(expected, param1):
    print("\nTesting '" + str(param1) + "'. (Expected = '" + str(expected) + "')")

    # Stores & prints out the final response
    response = dropMin(param1)
    print("'" + str(response) + "'")

    # Tells whether or not the test passed
    if response == expected:
        print("Passed")
    else:
        print("FAILED")


def main():
    tester([2, 3, 4, 5], [1, 2, 3, 4, 5])
    tester([2, 3, 4, 5], [2, 3, 4, 5, 1])
    tester([1, 1, 1, 1], [1, 1, 1, 1, 1])
    tester([], [1])
    tester([], [])
    tester([11111, 111111], [11111, 111111, 1234])
    tester([11111, 111111], [11111, 111111, -1234])
    tester([-11111, -1234], [-11111, -111111, -1234])


if __name__ == "__main__":
    main()
