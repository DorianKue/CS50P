from working import convert
import pytest


def test_convert_valid_no_min():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 PM to 7 AM") == "23:00 to 07:00"


def test_convert_valid_min():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("9:30 AM to 5:30 PM") == "09:30 to 17:30"


def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 9 PM")
