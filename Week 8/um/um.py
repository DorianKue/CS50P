import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Intializing an empty list to collect the "um"s from the input text.
    ums = []
    # Using \b and .findall to find all the "um" from the input text, case-insensitive.
    if matches := re.findall(r"\bum\b", s.lower()):
        # Simple for loop that appends each match, in this case "um", to the earlier initialized list.
        for match in matches:
            ums.append(match)
    # Returning the amount of "um"s found inside the "ums" list as an int using the .count() function.
    return ums.count("um")


if __name__ == "__main__":
    main()
