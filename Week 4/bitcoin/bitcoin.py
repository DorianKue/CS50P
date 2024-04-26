import json
import requests
import sys


def main():
    try:
        # Get user input from command-line arguments
        user_input = float(sys.argv[1])
    # If no argument is given, exit the program with an appropriate error message.
    except IndexError:
        sys.exit("Missing command-line argument")
    # If given argument cannot be converted to a float, exit the program with an approrpiate error message.
    except ValueError:
        sys.exit("Command-line argument is not a number")
    try:
        # Get the current price of bitcoin from the API
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        btc_json = response.json()
        btc_data = btc_json["bpi"]["USD"]
    # If there is a request issue, return nothing and exit the program.
    except requests.RequestException:
        return None
    # Extracting the bitcoin price from the previously fetched data and convert it to a float.
    btc_price = float(btc_data["rate"].replace(",", ""))
    # Calculating the total price by multiplying user input with the fetched bitcoin price.
    total_price = user_input * btc_price
    # Printing the result in the desired output format
    print(f"${total_price:,.4f}")


if __name__ == "__main__":
    main()
