import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
# Get all the available fonts as a list.
font_list = figlet.getFonts()


def main():
    # Checking if there are exactly 3 command-line arguments, the second is -f or --font and the third is available in the font_list.
    if (
        len(sys.argv) == 3
        and sys.argv[1] in ("-f", "--font")
        and sys.argv[2] in font_list
    ):
        # If the above is true, assigning the third argument to the chosen font, then asking for user input.
        user_font = sys.argv[2]
        user_input = input("Input: ")
        # Printing the ascii text with the specified font, using the "user_choice" function.
        print(user_choice(user_input, user_font))
    # If no command-line arguments are given, a random font is chosen using the random_choice function from the random module, and user is prompted for input.
    elif len(sys.argv) == 1:
        random_font = random.choice(font_list)
        user_input = input("Input: ")
        # Printing the ascii text in the randomly chosen font.
        print(user_choice(user_input, random_font))
    # If the command-line arguments are not in the expected format, the program exits.
    else:
        sys.exit("Invalid usage")


def user_choice(s, font):
    # Checking if the chosen font by the user is in the list of available fonts.
    if font in font_list:
        # If it is, setting the specified font, to then render the input text in ascii with the specified font and returning it.
        figlet.setFont(font=font)
        ascii_text = figlet.renderText(s)
        return ascii_text
    # If it's not available, exit the program.
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
