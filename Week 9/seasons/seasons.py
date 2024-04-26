from datetime import date
import inflect
import sys
p = inflect.engine()


def main():
    day_dffrnc = convert_days(get_input())
    # Converting the time difference in minutes from numerals into words, capitalizing the first letter, appending minutes and then printing the result.
    print(f"{p.number_to_words(day_dffrnc, andword="").capitalize()} minutes")


def get_input():
    # Get user input.
    user_in = input("Date of Birth: ")
    try:
        # Testing if the given input is in a valid ISO 8601 format.
        valid_in = date.fromisoformat(user_in)
        return valid_in
    # If given input is not in valid format, exit the program without raising an error, but giving an error message instead.
    except ValueError:
        sys.exit("Please enter your Date of Birth in YYYY-MM-DD format.")


def convert_days(t):
    # Calculating the difference between current date and user given date.
    day_dffrnc = date.today() - t
    # Converting the difference into minutes.
    minutes = day_dffrnc * 24 * 60
    # Returning the number of whole days in the difference as minutes.
    return minutes.days


if __name__ == "__main__":
    main()
