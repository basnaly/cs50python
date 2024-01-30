
from twttr import shorten

def test_lowercase_argument():
    assert shorten('about') == 'bt'

def test_lowercase_argument():
    assert shorten('about') == 'bt'

def test_uppercase_argument():
    assert shorten('Room') == 'Rm'

def test_number_argument():
    assert shorten('CS50python') == 'CS50pythn'

def test_punctuation_argument():
    assert shorten('hello, world') == 'hll, wrld'
