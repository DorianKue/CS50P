from fuel import convert, gauge
import pytest


# Test for valid input fractions.
def test_convert_valid_fraction():
    assert convert("0/4") == 0
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 100


# Test for invalid input fractions that should raise an error.
def test_convert_invalid_fraction():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("cat/dog")


# Test where the output should be "E" for an empty tank.
def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


# Test where the output should be "F" for a full tank.
def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


# Test for varying amounts of fuel.
def test_gauge_amount():
    assert gauge(13) == f"{13}%"
    assert gauge(33) == f"{33}%"
    assert gauge(66) == f"{66}%"


if __name__ == "__main__":
    main()
