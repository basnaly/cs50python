
from twttr import shorten

def test_argument():
    assert shorten('about') == 'bt'
    assert shorten('Room') == 'rm'
    assert shorten('CS50python') == 'cs50pythn'
    assert shorten('hello, world') == 'hll, wrld'
