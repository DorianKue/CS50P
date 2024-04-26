import sys

def main():
    # Initializing a variable to count the lines of code.
    line_count = 0
    # Exit the program if there are too few command-line arguments.
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # Exit the program if there are too many command-line arguments.
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Exit the program if the file isn't a python file.
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        try:
            # Opening the specified file in read mode.
            with open(sys.argv[1], "r") as file:
                for line in file:
                    # Remove leading whitespaces from the lines inside the file.
                    line = line.lstrip()
                    # If the line is empty or is a comment, skip to the next iteration of the loop.
                    if line == "" or line.startswith("#"):
                        continue
                    # Adding onto the earlier established variable for each valid line of code.
                    line_count += 1
        # Exiting the program if the file does not exist.
        except FileNotFoundError:
            sys.exit("File does not exist")
    # Printing out the LOC that are inside the file.
    print("Number of lines:", line_count)


if __name__ == "__main__":
    main()
