from bank import value


def test_uppercase_argument():
    assert input('Hi') == '$20'

def test_punctuation_argument():
    assert input('Hello, Sir') == '$0'
