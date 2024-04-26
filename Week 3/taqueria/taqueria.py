def main():
# dictionary of items and their respective prices.
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# defining a variable to keep track of the total cost, starting at $0.
    total_price = 0
    try:
# while loop to keep prompting the user for input until the program is stopped and making sure the input is titlecased as per the instructions.
        while True:
            item = input("Item: ").title()
# checking if the input "item" is in the dictionary "menu". if it is, updating the total_price variable and then displaying the current total cost.
            if item in menu:
                total_price += menu[item]
                print(f"Total: ${total_price:.2f}")
# error handling in case something unexpected like an integer is being inputted.
    except (KeyError, ValueError, TypeError):
        pass
# if ctrl + d is pressed to end the program, the error message won't be printed, instead the total price is printed in a new line.
    except EOFError:
        print(f"\nTotal: ${total_price:.2f}")


main()
