from um import count


def test_count_none():
    assert count("Hello, world!") == 0
    assert count("This is my favorite album.") == 0


def test_count_various_amount():
    assert count("Um?") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um, i don't know what to say, um...") == 3


def test_count_upper():
    assert count("UM, WHY AM I YELLING?") == 1
