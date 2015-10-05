"""
2015/09/17

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
The program takes in 5 number inputs from the user and will increment a single variable "total", that will be divided by 5
to print out the average of the 5 numbers.
"""

#Informs the user what will occur
print("The program will ask for 5 number inputs, and will calculate and print out the average for you (rounded to 2 decimal places)")


#Initialize a variable named "total" that is an integer, with the initial value of 0
total = 0.0

#Runs a loop 5 times
for i in range(1, 6):
    #Asks the user for a number input
    print("Please Enter Number " + str(i) + ":")

    #Adds the users input (assumed to be an integer) to the original value of "total"
    total = total + float(input())

#Prints out the average value of "total" (by dividing by 5)
print("\n" + "The average of the 5 numbers is: " + str(round(total/5, 2)))
