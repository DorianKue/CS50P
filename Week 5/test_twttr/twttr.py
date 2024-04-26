def main():
    # Asking user for input
    user_input = input("Input: ").strip()
    # Print shortened version of user input using the shorten function
    print(shorten(user_input), end="")
    # Printing a new line after the output to clean it up
    print("")


def shorten(word):
    # Establishing an empty string variable to store the shortened word in.
    shortened_word = ""
    # For loop iterating through each character.
    for c in word:
        # If the lowercase version of c is not a vowel, it is added to the variable shortened_word
        if c.lower() not in ["a", "e", "i", "o", "u"]:
            shortened_word += c
    # The shortened word is returned, omitting vowels.
    return shortened_word


if __name__ == "__main__":
    main()
