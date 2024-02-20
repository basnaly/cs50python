from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.deposit(6)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'


def test_deposit():
    jar = Jar()
    assert jar.deposit(3) == '🍪🍪🍪'


def test_withdraw():
    ...
