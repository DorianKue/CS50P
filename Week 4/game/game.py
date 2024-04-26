import random
import sys


def main():
    # Main loop to keep prompting the user for a valid input for the level.
    while True:
        try:
            lvl = int(input("Level: "))
            # Check if the level is valid and bigger than 0.
            if lvl > 0:
                # If the above is true, generating a random int within the range of 1 and the user input from level.
                random_int = random.randint(1, lvl)
                # Inner loop so that the user can keep guessing without it reverting back to the main loop and asking for a level input again.
                while True:
                    try:
                        # Prompting user for their guess input.
                        guess = int(input("Guess: "))
                        # If user input is too small.
                        if guess < random_int:
                            print("Too small!")
                            continue
                        # If user input is too large.
                        elif guess > random_int:
                            print("Too large!")
                            continue
                        # If user input is equal to the randomly generated int, "random_int", the program exits after printing out that the users guess was correct.
                        else:
                            sys.exit("Just right!")
                    # Handling ValueError exceptions in case the user input can not be converted to an integer.
                    except ValueError:
                        pass
            # If the level input is not valid, continue to the next iteration of the loop.
            else:
                continue
        # Again, handling a ValueError exception in case the user inputs something that can not be converted to an integer during the level selection.
        except ValueError:
            pass


if __name__ == "__main__":
    main()
