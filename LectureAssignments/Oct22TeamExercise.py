"""
2015/09/24

Group 2 Reversi, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
This code contains functions to move the first word in a sentence to the end, to reverse the sentence letter by letter and to reverse the sentence word by word
***Assumes smart user***
Additional known errors:
-does not validate inputs, will throw type error if invalid input is entered
-buffer could be exceeded in loops if parameters are too large
"""

# This is a function to move the first word of a sentence to the end of the sentence
# Params:
#		string - string to perform the operation only
# Return type: string 
def moveFirstWord(string):
	index = 0
	firstWord = ""
	string = string.strip()
	
	# loop through string until first space is found, signalling end of first word, then store everything before that index
	for x in string:
		# if first word found, ignore the rest of the iterations
		if firstWord == "":
			if string[index] == " ":
				firstWord = string[:index]
			index += 1
	
	#if no first word found, then return original string
	if firstWord != "":
		return string[index:].strip() + " " + firstWord
	else:
		return string
	
# This is a function to reverse a string word for word
# Params:
#		string - string to perform the operation only
# Return type: string 
def reverseSentence(string):
	string = string.strip()
	index = 0
	last = 0
	reversedstring =""
	
	for x in string:
		# if this index of the string includes a space, signal the end of a word, take that word, store the reverse
		# then, store the last character of that word 
		if string[index] == " ":
			reversedstring += " " + reverseString(string[last:index]).strip()
			last = index
		# if index is at the end, signal the end of word and repeat above
		if index == len(string) - 1:
			reversedstring += " " + reverseString(string[last:])
		index += 1
	
	# return string reversed so that it's back in left to right format
	return reverseString(reversedstring).strip()
	
def reverseString(string):
	reversed = ""
	for x in range(1, len(string) + 1):
		reversed += string[len(string) - x]
	return reversed
	
def main():
	print("Main program:")
	
	print("\nParam: ' There is no try, only do'")
	print(moveFirstWord(" There is no try, only do"))
	
	print("\nParam: 'Train yourself to let go of everything you fear to lose '")
	print(moveFirstWord("Train yourself to let go of everything you fear to lose "))
	
	print("\nParam: 'Fear    is the path to the dark side.'")
	print(moveFirstWord("Fear    is the path to the dark side."))
	
	print("\nParam: 'Powerful you have become,     the dark side I sense in you.'")
	print(moveFirstWord("Powerful you have become,     the dark side I sense in you."))
	
	print("\nParam: 'Hi '")
	print(moveFirstWord("Hi "))
	
	print("\nParam: 'there'")
	print(moveFirstWord("there"))
	
	print("\nParam: 'This Has 3 spaces'")
	print(moveFirstWord("This Has 3 spaces"))
	
	print("\nBonus:")
	
	print("\nParam:'Patience you must have my young padawan'")
	print(reverseSentence("Patience you must have my young padawan"))
	
	print("\nParam: ' There is no try, only do'")
	print(reverseSentence(" There is no try, only do"))
	
	print("\nParam: 'Train yourself to let go of everything you fear to lose '")
	print(reverseSentence("Train yourself to let go of everything you fear to lose "))
	
	print("\nParam: 'Fear    is the path to the dark side.'")
	print(reverseSentence("Fear    is the path to the dark side."))
	
	print("\nParam: 'Powerful you have become,     the dark side I sense in you.'")
	print(reverseSentence("Powerful you have become,     the dark side I sense in you."))
	
	print("\nParam: 'Hi '")
	print(reverseSentence("Hi "))
	
	print("\nParam: 'there'")
	print(reverseSentence("there"))
	
	print("\nParam: 'This Has 3 spaces'")
	print(reverseSentence("This Has 3 spaces"))
	
if __name__=="__main__":
	main()