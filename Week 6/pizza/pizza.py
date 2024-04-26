import csv
import sys
from tabulate import tabulate


def main():
    # Exit the program if there are too few command-line arguments.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # Exit the program if there are too many command-line arguments.
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Exit the program if the file isn't a CSV file.
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        # Initializing an empty list to later append the rows from the CSV file.
        pizzas = []
        file_name = sys.argv[1]
        try:
            # Opening the specified file in read mode.
            with open(file_name, "r") as file:
                # Creating a CSV reader object.
                reader = csv.reader(file)
                # Iterating over each row in the file and appending onto the "pizzas" list.
                for row in reader:
                    pizzas.append(row)
        # Exit the program if the file does not exist.
        except FileNotFoundError:
            sys.exit("File does not exist")
    # Printing everything out in the "grid" style from the tabulate package.
    print(tabulate(pizzas, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()
