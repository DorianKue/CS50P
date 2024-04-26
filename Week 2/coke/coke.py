def main():
# defining the accepted denominations of coins and setting the price
    accepted_coins = [5, 10, 25]
    total_paid = 0
    price = 50

# starting off and showing the price that has to be paid
    print(f"Amount Due: {price}")
# starting the "while" loop as long as the full price of 50 cents hasn't been paid yet
    while total_paid < price:
        coin = int(input("Insert Coin: "))
# making sure if the user input is correct and calculating the remaining price to pay or what the user is owed
        if coin in accepted_coins:
            total_paid += coin
            remaining_due = price - total_paid
            if remaining_due > 0:
                print(f"Amount Due: {remaining_due}")
            if total_paid >= price:
                amount_owed = total_paid - 50
                if amount_owed >= 0:
                    print(f"Change Owed: {amount_owed}")
# if something else than 5, 10 or 25 is being put in, simply printing the due amount again and ignoring the input, as if the coin leaves the vending machine again
        else:
            print(f"Amount Due: {price}")

main()
