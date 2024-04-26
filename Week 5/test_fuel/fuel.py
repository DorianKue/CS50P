def main():
    while True:
        # Prompt user for input.
        user_input = input("Fraction: ")
        try:
            # Attempting to convert the input
            fuel = convert(user_input)
            # If successful, break out of the loop.
            break
        except (ValueError, ZeroDivisionError):
            # Continuing to the next iteration if the conversion fails.
            continue
    # Printing the result.
    print(gauge(fuel))


def convert(fraction):
    # Splitting the fraction
    x, y = fraction.split("/")
    # Checking if both x and y are numerical.
    if x.isnumeric() and y.isnumeric():
        # Converting x and y into ints if they are numerical.
        x, y = int(x), int(y)
        z = x / y
        # Returning the converted decimal as a rounded percentage.
        return round(z * 100)
    # If y is zero, raise an error.
    elif int(y) == 0:
        raise ZeroDivisionError
    # if x and/or y are not an int, raise an error.
    else:
        raise ValueError


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
