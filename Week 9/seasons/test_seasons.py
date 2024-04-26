from datetime import date
from seasons import convert_days


def test_convert_days():
    assert convert_days(date.today()) == 0
