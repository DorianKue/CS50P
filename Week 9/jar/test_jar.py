from jar import Jar


def test_init():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4
    jar.deposit(7)
    assert jar.size == 11


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(6)
    assert jar.size == 6
    jar.withdraw(2)
    assert jar.size == 4
