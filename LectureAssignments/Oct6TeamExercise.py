"""
2015/10/06

Group 22, CPSC 231

Murray Cobbe Nathan Meulenbroek Sharjeel Junaid

Description: Includes a function to test a date for validity
"""


# Checks to see if any one date is valid
# Params:
#   dd - day in numerical value
#   mm - month in numerical value
#   yyyy - year in numerical value
# Implied:
#   All parameters are integers
def validateDate(dd, mm, yyyy):
    # Check that days or months aren't negative
    if dd < 1 or mm < 1 or mm > 12 or yyyy < 1:
        return False

    # Check that months with 31 days (Jan, Mar, May, July, Aug, Oct and Dec) don't have more than 31 days, else return False
    if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12) and dd > 31:
        return False

    # Check that months with 30 days (Apr, Jun, Sep, Nov) don't have more than 30 days, else return False
    if (mm == 4 or mm == 6 or mm == 9 or mm == 11) and dd > 30:
        return False

    # Check that February does not have more than 28 days on a normal year, 29 days on a normal year, else return False
    if mm == 2 and dd <= 29:
        # Follows rules for checking if leap year (any year divisible by 4 is a leap year except years divisible by 100 except years divisible by 400)
        if yyyy % 400 == 0 and dd != 29:
            return False
        elif yyyy % 100 == 0 and dd > 28:
            return False
        elif yyyy % 4 == 0 and dd != 29:
            return False
    elif mm == 2:
        return False

    # If none of the above conditions are true, return date is valid
    return True


# For testing only
def main():
    print(validateDate(28, 3, 1997))
    print(validateDate(229, 3, 1997))
    print(validateDate(29, 2, 2000))
    print(validateDate(29, 2, 1996))
    print(validateDate(29, 2, 1700))
    print(validateDate(31, 11, 1997))
    print(validateDate(31, 4, 1997))
    print(validateDate(10, 6, 1996))
    print(validateDate(28, 35, 1997))
    print(validateDate(14, 2, -1))


if __name__ == '__main__':
    main()
