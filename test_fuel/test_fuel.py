import pytest
from fuel import convert, gauge


def test_correct_argument():
    assert convert('3/4') == 75


def test_not_numeric_argument():
    with pytest.raises(ValueError):
        convert('cat/dog')


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


def test_full_argument():
    assert gauge(int('99')) == 'F'


def test_empty_argument():
    assert gauge(int('1')) == 'E'


def test_exist_persent():
    assert gauge(50) == '50%'
