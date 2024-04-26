from numb3rs import validate


def test_validate_valid_numbers():
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True

def test_validate_invalid_numbers():
    assert validate("-1.-1.-1.-1") == False
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("255.512.255.255") == False

def test_validate_ValueError():
    assert validate("cat") == False
