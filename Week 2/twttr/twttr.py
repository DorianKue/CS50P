def main():
    msg = input("Input: ")
# defining the list of vowels
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# iterating over each letter of the "msg" value
    for c in msg:
# checking if "c" is not a vowel, if it isn't then printing it without starting a new line
        if c not in vowels:
            print(c, end="")
    print("")

main()
