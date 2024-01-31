import pytest
from fuel import convert, gauge

def test_correct_argument():
    assert convert('3/4') == 75

# def test_not_numeric_argument():
#     assert convert('cat/dog') == AttributeError

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        assert convert('1/0') == ZeroDivisionError

def test_full_argument():
    assert gauge(int('99')) == 'F'


def test_empty_argument():
    assert gauge(int('1')) == 'E'

