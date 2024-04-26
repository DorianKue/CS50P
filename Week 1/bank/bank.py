def main():
    x = input("Greeting: ").lower().strip()
    if greetings(x):
        print("$0")
    elif inc_h(x):
        print("$20")
    else:
        print("$100")


def greetings(hello):
    if hello.startswith("hello"):
        return True
    else:
        return False

def inc_h(h):
    if h.startswith("h"):
        return True
    else:
        return False

main()
