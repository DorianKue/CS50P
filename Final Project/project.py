import random  # Importing the random module to generate random coin toss results.
import csv  # Importing the csv module to handle CSV file operations.
import sys  # Importing the sys module to access system-specific parameters and functions.
import os  # Importing the os module to interact with the operating system.
import math  # Importing the math module to calculate the odds of the coin tosses.


def main():
    """Main function to run the coin toss simulation and handle user interaction."""
    coin_toss_amount = (
        get_input()
    )  # Getting the number of times the user wants to flip the coin.
    results = get_results(coin_toss_amount)  # Generating coin toss results.
    heads_count, heads_percentage, tails_count, tails_percentage = analyze_results(
        results
    )  # Analyzing the results.
    # Printing the analysis results.
    print(f"Heads: {heads_count} times which is {heads_percentage:.2f}%")
    print(f"Tails: {tails_count} times which is {tails_percentage:.2f}%")
    probability_percent = get_odds(
        heads_count, tails_count
    )  # Calculating the odds of outcome.
    print(f"The odds of this outcome are {probability_percent:.2f}%")
    save_results = input(
        "Would you like to save these results? y/n "
    )  # Asking the user if they want to save the results.
    if save_results.lower() in [
        "y",
        "yes",
    ]:  # Checking if the user wants to save the results.
        # If yes, write the results to a CSV file.
        write_results(
            coin_toss_amount,
            heads_count,
            heads_percentage,
            tails_count,
            tails_percentage,
            probability_percent,
        )
        sys.exit(
            "Results saved to flip_results.csv..."
        )  # Exiting the program with a message, indicating that results were saved.
    else:
        sys.exit(
            "Results were not saved. Exiting program..."
        )  # Exiting the program with a message, indicating that results were not saved.


def get_input():
    """Function to get the number of times the user wants to flip the coin."""
    while True:
        try:
            coin_toss_amount = int(
                input("How many times would you like to flip the coin? ")
            )  # Asking the user for input.
            if (
                coin_toss_amount <= 0
            ):  # Checking if the input is less than or equal to zero.
                print("Please enter a positive number")  # Printing an error message.
            else:
                return coin_toss_amount  # Returning the valid input.
        except ValueError:
            print(
                "Please enter a valid number"
            )  # Printing an error message for invalid input.


def get_results(n):
    """Function to generate coin toss results."""
    results = []  # Initializing an empty list to store the results.
    for _ in range(n):  # Iterating n times.
        results.append(
            random.choice(["Heads", "Tails"])
        )  # Appending a random result (Heads or Tails) to the list.
    return results  # Returning the list of results.


def analyze_results(results):
    """Function to analyze the coin toss results."""
    heads_count = results.count("Heads")  # Counting the number of Heads.
    tails_count = results.count("Tails")  # Counting the number of Tails.
    total_count = len(results)  # Calculating the total number of tosses.
    if total_count > 0:  # Checking if there are toss results.
        heads_percentage = (
            heads_count / total_count
        ) * 100  # Calculating the percentage of Heads.
        tails_percentage = (
            tails_count / total_count
        ) * 100  # Calculating the percentage of Tails.
        return (
            heads_count,
            heads_percentage,
            tails_count,
            tails_percentage,
        )


def get_odds(heads, tails):
    """Function to calculate the odds of the outcome."""
    # Calculating the total number of coin flips.
    total_flips = heads + tails
    # If no flips were done, return 0%.
    if total_flips == 0:
        return 0.0
    # Determining the count of the less frequent outcome.
    lfo_count = min(heads, tails)
    # Calculating the number of combinations using the binomial coefficient (n choose k) formula.
    nCk = math.factorial(total_flips) / (
        math.factorial(lfo_count) * math.factorial(total_flips - lfo_count)
    )
    # Calculating the probability of the outcome.
    prob = nCk / (2**total_flips)
    # Finally converting the probability to percent and returning it.
    prob_percent = prob * 100
    return prob_percent


def write_results(
    coin_toss_amount,
    heads_count,
    heads_percentage,
    tails_count,
    tails_percentage,
    probability_percent,
):
    """Function to write the results to a CSV file."""
    file_exists = os.path.exists("flip_results.csv")  # Checking if the CSV file exists.
    with open(
        "flip_results.csv", "a", newline=""
    ) as file:  # Opening the CSV file in append mode.
        fieldnames = [
            "total_flips",
            "heads_count",
            "heads_percentage",
            "tails_count",
            "tails_percentage",
            "probability_percent",
        ]  # Defining the fieldnames for the CSV.
        writer = csv.DictWriter(
            file, fieldnames=fieldnames
        )  # Creating a CSV writer object.
        if not file_exists:  # Checking if the CSV file exists.
            writer.writeheader()  # Writing the header row.
        # Writing a row with the results.
        writer.writerow(
            {
                "total_flips": coin_toss_amount,
                "heads_count": heads_count,
                "heads_percentage": round(heads_percentage, 2),
                "tails_count": tails_count,
                "tails_percentage": round(tails_percentage, 2),
                "probability_percent": round(probability_percent, 2),
            }
        )


if __name__ == "__main__":
    main()
