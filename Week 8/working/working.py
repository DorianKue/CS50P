import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Checking if the input matches one of the expected formats and seperating the times and "AM" or "PM" into seperate groups.
    if matches := re.search(
        r"^([\d]{1,2}(?::[\d]{1,2})?)\s{1}([A-Z]{2})\s{1}to\s{1}([\d]{1,2}(?::[\d]{1,2})?)\s{1}([A-Z]{2})$",
        s,
    ):
        # Extracting the start and end times together with "AM" or "PM" from the groups.
        start_time = matches.group(1)
        start_ampm = matches.group(2)
        end_time = matches.group(3)
        end_ampm = matches.group(4)

        # Converting the input time to 24 hour format.
        converted_start_time = convert_to_24(start_time, start_ampm)
        converted_end_time = convert_to_24(end_time, end_ampm)
        # Returning the converted time range to the main function to then print it out.
        return f"{converted_start_time} to {converted_end_time}"
    else:
        raise ValueError


def convert_to_24(s, ampm):
    # If no minutes were given, only convert hours.
    if ":" not in s:
        hours = int(s)
        if hours > 12:
            raise ValueError
        if ampm == "AM":
            # Convert 12 AM to 00:00
            if hours == 12:
                hours = 0
        else:
            # Converting "PM" time to the 24 hour format.
            if hours != 12:
                hours += 12
        # Return the converted time.
        return f"{hours:02}:00"
    else:
        # If the inputted time has minutes then split the hours and minutes and convert them into integers.
        hours, min = s.split(":")
        hours, min = int(hours), int(min)
        # If either hours or minutes are outside of the specified range, an error is raised.
        if hours > 12 or min > 59:
            raise ValueError
        # Converting "PM" time to 24 hour format.
        if ampm == "PM" and hours != 12:
            hours += 12
        # Converting "AM" time to 24 hour format and if applicable, convert 12:XX AM to 00:XX.
        elif ampm == "AM" and hours == 12:
            hours = 0
        # Return the converted time, including minutes.
        return f"{hours:02}:{min:02}"


if __name__ == "__main__":
    main()
