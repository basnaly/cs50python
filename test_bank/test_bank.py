from bank import value


def test_uppercase_argument():
    assert value('Hi') == '20'

def test_punctuation_argument():
    assert value('Hello, Sir') == '0'
