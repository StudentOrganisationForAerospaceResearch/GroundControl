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
-does not validate inputs, will throw type error if invalid input is entered
"""

# A funciton to replace any spaces in a string with the desired replacement string
# Params:
#		str - the string to replace things from
#		replacement - the string to replace spaces with
#	Return:
#		string - result of spaces being removed and replaced with 'replacement'
def replaceSpaces(str, replacement):
	# ***Code with bug introduced for class requirements. 
	# ***Will cause an error with any test case that has a space, as strings are not mutable
	# ***Test case: str = 'hello there' replacement='123'
	# ***Debugging techniques used: None, but we would have looked for where we're assigning str in some way that was improper based on the error
	#index = 0
	#for x in str:
	#	if x == " ":
	#		str[0] = replacement
	#index += 1
	#return str
	
	
	result = ""
	# loops through characters in str, concatenates to string result the desired character
	for x in str:
		if x == " ":
			result = result + replacement
		else:
			result = result + x
	return result
	
def main():
	#Test 1 space and multiple following spaces
	print( "\nParams: 'hello there      ', '123'")
	print("Result:" + replaceSpaces("hello there      ", "123"))
	#Test leading space and trailing space
	print( "\nParams: ' hello there      ', '123'")
	print("Result:" + replaceSpaces(" hello there      ", "123"))
	#Test spaces every other character
	print( "\nParams: ' h e l l o t h e r e ', '123'")
	print("Result:" + replaceSpaces(" h e l l o t h e r e ", "123"))
	#Test replacement string having spaces
	print( "\nParams: 'hello there      ', '1 2 3'")
	print("Result:" + replaceSpaces("hello there      ", "1 2 3"))
	#Test no spaces
	print( "\nParams: 'hellothere', '123'")
	print("Result:" + replaceSpaces("hellothere", "123"))
	#Test empty string
	print( "\nParams: '', '123'")
	print("Result:" + replaceSpaces("", "123"))

if __name__=='__main__':
	main()