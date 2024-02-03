import pytest

from fuel import convert, gauge


def test_corrected_argument():
    assert convert('1/2') == 50

cd lines
def test_str_argument():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_empty_argument():
    assert gauge(int('1')) == 'E'


def test_full_argument():
    assert gauge(int('99')) == 'F'


def test_persantage_argument():
    assert gauge(int('75')) == '75%'
