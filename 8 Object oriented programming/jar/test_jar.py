import pytest
from jar import Jar

def test_init():
    # Test default initialization
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # Test initialization with specific capacity
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # Test initialization with invalid capacity
    with pytest.raises(ValueError):
        jar = Jar(-1)
    with pytest.raises(ValueError):
        jar = Jar("a string")

def test_str():
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

    # Test string representation when the jar is full
    with pytest.raises(ValueError):
        jar.deposit(1)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(2)
    assert jar.size == 5

    # Test deposit beyond capacity
    with pytest.raises(ValueError):
        jar.deposit(1)

def test_withdraw():
    jar = Jar(5)

    jar.deposit(3)
    jar.withdraw(1)
    assert jar.size == 2

    jar.withdraw(2)
    assert jar.size == 0

    # Test withdraw more than available
    with pytest.raises(ValueError):
        jar.withdraw(1)

if __name__ == "__main__":
    pytest.main()
