# Ask the user for input and check if the plate is valid using the is_valid function. If it is, print Valid, if it isn't, print Invalid.
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
# Checking if the length of the plate is correct, in this case between two and six characters long, starts with two letters and only consist of numbers and letters and not special characters.
    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():
        has_number = False
# If the plate passed the first check and only consist of letters, it is valid and doesn't require any further checks.
        if s.isalpha():
            return True
# Looping through each character and checking if a character is a number
        for c in s:
            if c.isnumeric():
                has_number = True
# Checking if the number doesn't start with 0 and if the remaining chracters are numbers. If that's the case, the plate is valid. If not, it's invalid.
                if s[s.index(c):].isnumeric() and c != "0":
                    return True
                else:
                    return False
# If the plate fails the first check, it is invalid by default because it doesn't start with 2 letters.
    else:
        return False


main()


#def main():
#    plate = input("Plate: ")
#    if is_valid(plate):
#        print("Valid")
#    else:
#        print("Invalid")
#
#
#def is_valid(s):
#    if 2 <= len(s) <= 6 and s.isalnum() and s[:2].isalpha():
#        has_number = False
#        if s.isalpha():
#            return True
#        for c in s:
#            if c.isnumeric():
#                has_number = True
#                if s[s.index(c):].isnumeric() and c != "0":
#                    return True
#                else:
#                    return False
#    else:
#        return False
#
#main()

# s.index(c): This part of the code is finding the index of the character c within the string s. In simpler terms, it's figuring out where in the string s the character c is located. For example, if s is "AB123", and c is "1", s.index(c) would return 2 because "1" is at index 2 in the string "AB123".
#
# s[s.index(c):]: This part of the code is slicing the string s from the index where c is found till the end of the string. So, if c is "1" and s is "AB123", s[s.index(c):] would return "123". This is essentially extracting the part of the string that starts from the first occurrence of the character c till the end of the string.
#
# .isnumeric(): This is a method that checks if all the characters in a string are numeric (i.e., digits). If all characters in the sliced portion of the string (from the first occurrence of c till the end) are numeric, then .isnumeric() will return True. If any non-numeric characters are found, it will return False.
#
# and: This is a logical operator that combines two conditions. In this case, it means that both conditions on either side of and must be True for the whole expression to be True.
#
# c != "0": This is a comparison that checks if the character c is not equal to "0". In other words, it's making sure that c is not the digit zero.
#
# So, putting it all together:
#
# The line if s[s.index(c):].isnumeric() and c != "0": is checking if:
#
# All the characters in the portion of the string s starting from the first occurrence of c till the end are numeric (i.e., digits).
# The character c itself is not equal to "0".
# If both conditions are true, then the overall expression evaluates to True, otherwise, it evaluates to False.
