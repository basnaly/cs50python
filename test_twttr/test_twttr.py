
from twttr import shorten

def test_argument():
    assert shorten('about') == 'bt'
    assert shorten('Room') == 'Rm'
    assert shorten('CS50python') == 'CS50pythn'
    assert shorten('hello, world') == 'hll, wrld'
