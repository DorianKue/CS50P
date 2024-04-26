def main():
# getting the fuel as a fraction from the get_fuel_percent function and converting it to %.
    fuel = get_fuel_percent()
    fuel_percent = round(fuel * 100)
# checking if the percentage is more than 1% and less than 99%. If that's the case printing the remaining fuel percentage.
    if 1 < fuel_percent < 99:
        print(f"{fuel_percent}%")
# checking if the percentage is greater or equal to 99% and printing "F" if it is.
    elif 99 <= fuel_percent:
        print("F")
# if neither of the above is the case and fuel is 1% or less, printing "E".
    else:
        print("E")


def get_fuel_percent():
# inducing a loop that keeps asking for input if an error is found.
    while True:
        try:
            prompt = input("Fraction: ")
# splitting the input into x and y and converting x and y into an int, then calculating the fraction
            x, y = prompt.split("/")
            x = int(x)
            y = int(y)
            z = x / y
# if the result of x / y is less or equal to 1, returning it to the main function.
            if z <= 1:
                return z
# catching possible errors like an invalid input or a zero division error but then passing it, asking for the input of the user again
        except (ValueError, NameError, ZeroDivisionError, TypeError):
            pass


main()
