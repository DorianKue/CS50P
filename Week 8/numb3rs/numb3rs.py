import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Match each character to see if it is between 0-9 and do this 1-3 times per "block" of numbers before a ".", then match the "." and repeat the process 3 more times to match the format of an IPv4 address.
    # If the matching fails, return False.
    if not re.search(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}", ip):
        return False
    # Splitting the input ip address into its individual "blocks" of numbers.
    num_blocks = ip.split(".")
    # Checking if there are more than 4 "blocks" of numbers. If there are, return False because an IPv4 address should have exactly 4 blocks.
    if len(num_blocks) > 4:
        return False
    for num_block in num_blocks:
        try:
            # Check each block of code if it is inside a valid range, between 0-255, using a for loop. Returning False if a number is below 0 or above 255, because that would be an invalid IPv4 address.
            if int(num_block) < 0 or int(num_block) > 255:
                return False
        # If there is a ValueError because the input could not be converted to an int, like "cat" for example, return False.
        except ValueError:
            return False
    # If all checks are passed, return True, because the inputted IPv4 address is valid.
    return True


if __name__ == "__main__":
    main()
