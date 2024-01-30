
from twttr import shorten

def test_argument():
    assert shorten('about') == 'bt'
    #assert shorten('twitter') != 'twitter'
