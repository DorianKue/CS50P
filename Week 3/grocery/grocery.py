def main():
# Creating an empty dictionary to store the inputted items and their amount.
    grocery_list = {}
# Starting an infinite loop inside the try block until the program is stopped by pressing ctrl + D, which also handles KeyErrors.
    try:
        while True:
# User input is handled case insensitively while removing leading and trailing whitespaces.
                item = input().lower().strip()
# If the inputted item isn't already in the grocery_list dict, it is added to it with an amount, or value of 1. If the item already is present in the dict, +1 is added to its amount.
                if item not in grocery_list:
                    grocery_list[item] = 1
                else:
                    grocery_list[item] += 1
    except KeyError:
        pass
# If ctrl + D is pressed, a for loop iterates over the keys inside the dict and sorts them alphabetically. It then accesses the value, amount, inside the dictionary and the list is printed in uppercase.
    except EOFError:
        for item in sorted(grocery_list):
            amount = grocery_list[item]
            print(f"{amount} {item.upper()}")

main()

