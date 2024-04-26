# Importing the value function from bank.py
from bank import value


# Testing to see if the return value is 0 if the input contains case-insensitive "hello".
def test_greeting_hello():
    assert value("hello") == 0
    assert value("Hello, name") == 0


# Testing if the greeting starts with an "h", case-insensitive.
def test_greeting_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("How are you?") == 20


# Testing if the greeting doesn't contain "h" or starts with "hello" and returns the correct value.
def test_no_h():
    assert value("What's up?") == 100
    assert value("Yo") == 100


if __name__ == "__main__":
    main()
