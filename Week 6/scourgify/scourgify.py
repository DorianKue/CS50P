import csv
import sys


def main():
    # Exit the program if there are too few command-line arguments.
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # Exit the program if there are too many command-line arguments.
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Exit the program if the file isn't a CSV file.
    elif ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    else:
        # Establishing variables for the command-line arguments and initializing an empty list to store and clean up the data from the input file.
        before_csv_name = sys.argv[1]
        after_csv_name = sys.argv[2]
        students = []
        try:
            # Opening up the input CSV to read from it.
            with open(before_csv_name) as before_file:
                reader = csv.DictReader(before_file)
                for row in reader:
                    # Iterating over each row in the CSV file and cleaning it up by removing the double quotation marks from the names.
                    name = row["name"].replace('"', "")
                    # Splitting the name into first and last name.
                    last, first = name.split(",")
                    # Removing trailing whitespaces from the first names.
                    first = first.lstrip()
                    # Appending the cleaned up data into the earlier creater "students" list.
                    students.append(
                        {
                            "first": first,
                            "last": last,
                            "house": row["house"],
                        }
                    )
        # Exiting the program if the input file could not be found.
        except FileNotFoundError:
            sys.exit(f"Could not read {before_csv_name}")

    # Writing the cleaned up data to a new CSV file.
    with open(after_csv_name, "w") as after_file:
        # Initializing the CSV writer with fieldnames, then writing the header row with those.
        writer = csv.DictWriter(after_file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        # Writing each students name and house into the new CSV file.
        for student in students:
            writer.writerow(student)


if __name__ == "__main__":
    main()
