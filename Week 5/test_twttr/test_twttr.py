# Importing the shorten function from the twttr module
from twttr import shorten


# Testing for words with no vowels and making sure nothing is being omitted.
def test_shorten_no_vowels():
    assert shorten("Crypt") == "Crypt"


# Testing for words with vowels and making sure that the vowels are being omitted.
def test_shorten_with_vowels():
    assert shorten("Twitter") == "Twttr"


# Testing only vowels in lowercase, making sure the output is nothing.
def test_shorten_vowels_lower():
    assert shorten("aeiou") == ""


# Testing only vowels in uppercase.
def test_shorten_vowels_upper():
    assert shorten("AEIOU") == ""


# Making sure no numbers are being omitted.
def test_shorten_numbers():
    assert shorten("123") == "123"


# Making sure no punctuation is being omitted.
def test_shorten_punctuation():
    assert shorten(".!?,") == ".!?,"


if __name__ == "__main__":
    main()
