from plates import is_valid


# Testing for valid length and only alphabetical characters.
def test_is_valid_isalpha_validlength():
    assert is_valid("SHORT") == True
    assert is_valid("short") == True


# Testing for invalid length(too long) and only alphabetical characters.
def test_is_valid_isalpha_too_long():
    assert is_valid("THISISTOOLONG") == False
    assert is_valid("thisistoolong") == False


# Testing for invalid length(too short) and only alphabetical characters.
def test_is_valid_isalpha_too_short():
    assert is_valid("x") == False


# Testing for valid length, including numericals, that is a valid plate.
def test_is_valid_has_number_validlength():
    assert is_valid("CS50") == True
    assert is_valid("cs404") == True


# Testing for valid length, including numericals, that is an invalid plate because the first number is a zero.
def test_is_valid_has_number_startswith_zero():
    assert is_valid("CS05") == False


# Testing for valid length, including numericals, but it only contains or starts with numericals, thus an invalid plate.
def test_is_valid_startswith_number():
    assert is_valid("05CS") == False
    assert is_valid("50") == False


# Testing for non alphanumeric inputs, which should output an invalid plate.
def test_is_valid_non_alnum():
    assert is_valid("!!!") == False
    assert is_valid("CS50!") == False
    assert is_valid("!cs50") == False


# Testing for valid length, including valid number placement, but alphabetical characters after numeric characters, which should output invalid.
def test_is_valid_number_placement():
    assert is_valid("CS50YO") == False


if __name__ == "__main__":
    main()
