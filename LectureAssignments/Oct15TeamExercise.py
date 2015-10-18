"""
2015/09/24

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This code has been proofread from 'http://pages.cpsc.ucalgary.ca/~verwaal/average.txt'
***Assumes smart user***
Additional known errors:
-buffer limit can be exceeded if too many values entered
-does not check for null input error
-does not validate that input is numerical
"""

# A function to check if the input grade is a valid GPA - returns boolean
# Params:
#		grade - numerical floating point value
def isValidGrade(grade) :
   # LOGIC ERROR: was 0 and 4.3 exclusive, must be inclusive. 
   # TEST: Input 4.3 or 0 to reproduce with old code. Assumes the error directly below has been fixed
   #return grade > 0 and grade < 4.3
   return grade >= 0 and grade <= 4.3
   
# A function to check if the input grade is a valid GPA - returns float
def getGrade() :
   grade = float(input("Enter a letter grade point value (or -1 to quit): "))
   
   # LOGIC ERROR:  the 'or' should be an and, otherwise when they don't want to quit, they're being kept in the loop
   # TEST: Input any valid input, and you get stuck in the loop
   #while (grade != -1 or not isValidGrade(grade)) :
   
   # loops through asking for new input while -1 is not entered or input is not valid
   while (grade != -1 and not isValidGrade(grade)) :
      print(grade, "is not valid.  A letter grade point value must be between 0 and 4.3.")
      grade = float(input("Enter a letter grade point value (or -1 to quit): "))
   
   return grade
   
# A function to check if the input grade is a valid GPA - returns float
def average() :
   grade = getGrade()
   sum = 0.0
   # LOGIC ERROR: counter should start at 0, not 1. 
   # TEST: Input any valid number, and then put in -1 to exit, the code returns a value that's too small. Assumes the two errors above have been fixed.
   # counter = 1
   counter = 0
   
   # loops through summing inputs and counting inputs until the value -1 is entered
   while (grade != -1) :
      counter = counter + 1
      sum = sum + grade
      # LOGIC ERROR: not storing the return from getGrade()
	  # TEST: Input -1 after at least 1 input. Assumes errors above have been fixed
      #getGrade();
      grade = getGrade()
	
   # LOGIC ERROR: counter can not be 0 when you divide
   # TEST: enter -1 on first input
   #return sum/counter
   
   # Verifies that we're not dividing by 0
   if counter != 0:
      average = sum/counter
      return average
   
   return 0
      
print(average())