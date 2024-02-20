from jar import Jar


def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ''
    jar.deposit(2)
    assert str(jar) == '🍪🍪'
    jar.deposit(6)
    assert str(jar) == '🍪🍪🍪🍪🍪🍪'


def test_deposit():
    ...


def test_withdraw():
    ...
