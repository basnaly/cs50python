import pytest

from fuel import convert, gauge


def test_corrected_argument():
    assert convert('1/2') == 50


def test_str_argument():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')
