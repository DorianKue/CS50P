# Importing the validators library.
import validators


def main():
    # Asking user for their email address as input, then calling is_valid function with that input.
    print(is_valid(input("What's your email address? ")))


def is_valid(s):
    # Using the validators library to check if the inputted email address is valid. If it is, it returns True and thus returns "Valid" to the main function. If it returns False, then "Invalid" is returned to main.
    if validators.email(s):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
