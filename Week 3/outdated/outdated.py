def main():
    # Creating a dict that stores the months as keys and associates the respective number with it.
    months = {
        "January": "01",
        "February": "02",
        "March": "03",
        "April": "04",
        "May": "05",
        "June": "06",
        "July": "07",
        "August": "08",
        "September": "09",
        "October": "10",
        "November": "11",
        "December": "12",
    }

    # Starting an infinite loop that ask the user for input and strips it from any leading and trailing whitespaces.
    while True:
        user_date = input("Date: ").strip()
        # If "/" is found within the input, the input will be split and stored inside new variables while the days and months are being padded with a 0 if necessary.
        if "/" in user_date:
            try:
                month, day, year = user_date.split("/")
                month = month.zfill(2)
                day = day.zfill(2)
                # If the variables are within a valid range of days, months and years, the date is printed in the ISO 8601 format and the loop breaks. If not, the input is being ignored and the user  is prompted again.
                if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 0 <= int(year):
                    print(f"{year}-{month}-{day}")
                    break
            except (ValueError, TypeError):
                pass

        # If no comma is found within the input, for example when the user types "September 8 1636" the input will be ignored and user will be reprompted.
        elif "," not in user_date:
            pass

        # If none of the above is applicable, the input will be something like "October 9, 1701". The input is then stripped of any "," and split, to be stored inside variables again.
        else:
            try:
                month, day, year = user_date.replace(",", "").split(" ")
            except (ValueError, TypeError):
                pass
            else:
                # Pad the day variable with a 0 if necessary and then checking if the month and year are within a valid range.
                day = day.zfill(2)
                if month in months and 1 <= int(day) <= 31 and 0 <= int(year):
                    # Printing the date in ISO 8601 format and breaking the loop.
                    print(f"{year}-{months[month]}-{day}")
                    break


main()
