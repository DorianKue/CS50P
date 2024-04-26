def main():
# asking for user input
    camel = input("camelCase: ")
# printing the required "snake_case" output and adding the end parameter so that it won't default to a new line
    print("snake_case: " , end="")
# for loop looking for lowercase characters and printing them out
    for c in camel:
        if c.islower():
            print(c, end="")
# if an uppercase charachter is found, printing an underscore and converting the uppercase to lowercase
        else:
            print("_" + c.lower(), end="")
    print("")

main()
