from jar import Jar
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.deposit(6)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    jar.deposit(3) == '🍪🍪🍪'
    assert jar.capacity > jar.size
    with pytest.raises(ValueError):
        assert jar.deposit(10)


def test_withdraw():
    jar == 
