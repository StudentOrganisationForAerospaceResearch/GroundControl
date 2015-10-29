"""
2015/10/27

Group 22, CPSC 231

Murray Cobbe
Nathan Meulenbroek
Sharjeel Junaid

Description:
Three different functions to count the number of occurrences of one string in another
"""
# A function to count the number of characters in a string
# Params:
#   string - the string to be searched
#   search - the string to be searched for
# Return:
#   int - number of occurrences of search in string
def count1(string, search):
    count = 0
    for x in string:
        if x == search:
            count += 1
    return count

# A function to count the number of characters in a string
# Params:
#   string - the string to be searched
#   search - the string to be searched for
# Return:
#   int - number of occurrences of search in string
def count2(string, search):
    count = 0
    for x in range(len(string)):
        if string[x] == search:
            count += 1
    return count

# A function to count the number of characters in a string
# Params:
#   string - the string to be searched
#   search - the string to be searched for
# Return:
#   int - number of occurrences of search in string
def count3(string, search):
    index = 0
    count = 0

    while index < len(string):
        if string[index] == search:
            count += 1
        index += 1

    return count

#Tester code
def main():
    #Test count1
    print("Test algorithm 1")

    print("Params: 'abracadabra' & 'a'")
    print("Expected: 5")
    print(count1("abracadabra", "a"))

    print("Params: ' a b r a c a d a b r a ' & 'a'")
    print("Expected: 5")
    print(count1(" a b r a c a d a b r a ", "a"))

    print("Params: 'abracadabra' & ''")
    print("Expected: 0")
    print(count1("abracadabra", ""))

    print("Params: '' & 'a'")
    print("Expected: 0")
    print(count1("", "a"))

    print("Params: 'abracadabra' & 'e'")
    print("Expected: 0")
    print(count1("abracadabra", "e"))

    #Test count2
    print("Test algorithm 2")

    print("Params: 'abracadabra' & 'a'")
    print("Expected: 5")
    print(count2("abracadabra", "a"))

    print("Params: ' a b r a c a d a b r a ' & 'a'")
    print("Expected: 5")
    print(count2(" a b r a c a d a b r a ", "a"))

    print("Params: 'abracadabra' & ''")
    print("Expected: 0")
    print(count2("abracadabra", ""))

    print("Params: '' & 'a'")
    print("Expected: 0")
    print(count2("", "a"))

    print("Params: 'abracadabra' & 'e'")
    print("Expected: 0")
    print(count2("abracadabra", "e"))

    #Test count3
    print("Test algorithm 3")

    print("Params: 'abracadabra' & 'a'")
    print("Expected: 5")
    print(count3("abracadabra", "a"))

    print("Params: ' a b r a c a d a b r a ' & 'a'")
    print("Expected: 5")
    print(count3(" a b r a c a d a b r a ", "a"))

    print("Params: 'abracadabra' & ''")
    print("Expected: 0")
    print(count3("abracadabra", ""))

    print("Params: '' & 'a'")
    print("Expected: 0")
    print(count3("", "a"))

    print("Params: 'abracadabra' & 'e'")
    print("Expected: 0")
    print(count3("abracadabra", "e"))

    return

if __name__=="__main__":
    main()