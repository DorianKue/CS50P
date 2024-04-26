# Importing the emoji module
import emoji


def main():
    # Asking user for input
    user_input = input("Input: ")
    # Using the emojize function to convert any code or aliases into their corresponding emoji.
    # The language = "alias" section enables the use of both the full list and aliases as per the documentation.
    output = emoji.emojize(user_input, language="alias")
    # Printing the converted input.
    print(output)


if __name__ == "__main__":
    main()
