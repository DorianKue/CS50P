import random


def main():
    # Prompt the user for a level of difficulty.
    level = get_level()
    # Variable to keep track of the users correct answers.
    score = 0
    # Loop through ten math problems using a for loop.
    for _ in range(10):
        # Generating two random int numbers based on the chosen level, then calculating the correct answer for the generated problem.
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        # Formatting the generated problem to display it to the user.
        problem = f"{x} + {y} = "
        # Variable to keep track of the users attempts to solve a given problem.
        attempts = 0
        # User can attempt give problem up to 3 times.
        while attempts < 3:
            try:
                # Prompt user for an answer to the given problem.
                user_answer = int(input(problem))
                # Checking if the given answer is correct. If it is, add +1 to the score
                if user_answer == correct_answer:
                    score += 1
                    break
                # If given answer is incorrect, printing "EEE" as specified and adding +1 to attempts.
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                pass
        # Print the correct answer to the given problem if the user has failed three times.
        else:
            print(f"{x} + {y} = {correct_answer}")
    # Displaying the final score.
    print(f"Score: {score}")


def get_level():
    # Ask user for level of difficulty until a valid input is given.
    while True:
        try:
            level = input("Level: ")
            # If valid input is given, return the input as an int.
            if level in ["1", "2", "3"]:
                return int(level)
        except ValueError:
            pass


def generate_integer(level):
    # Generate a random int based on the chosen level by the user and returning it.
    try:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)
        else:
            raise ValueError
    except ValueError:
        pass


if __name__ == "__main__":
    main()
