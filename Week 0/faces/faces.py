# Defining the main function which takes user input, calls on the convert function and prints the result
def main():
    inputmsg = input("Type your message here: ")
    outputmsg = convert(inputmsg)
    print(outputmsg)

# Defining the convert function to replace the emoticons with emoji
def convert(inputmsg):
    return inputmsg.replace(":)", "🙂").replace(":(", "🙁")


main()
