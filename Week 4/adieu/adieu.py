import inflect

# Initializing the inflect engine as per the documentation.
p = inflect.engine()
# Creating an empty list to store the inputted names.
names = []


def main():
    try:
        # Continue prompting the user for names until Ctrl + D (EOFError) is pressed.
        while True:
            user_input = input("Name: ")
            # Add the inputted name to the end of the list using the .append() function.
            names.append(user_input)
    # When Ctrl + D is pressed, the loop ends and the specified output is printed in a new line using the p.join() function from the imported inflect module.
    except EOFError:
        print("\nAdieu, adieu, to", p.join(names))


if __name__ == "__main__":
    main()
