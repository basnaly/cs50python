from working import convert
import pytest


def test_corrected_version():
    assert convert('8 AM to 7 PM') == '08:00 to 19:00'


def test_incorrect_version():
    with pytest.raises(ValueError):
        convert('7:20 AM to 8:60 PM')


def test_omit_minutes():
    with pytest.raises(ValueError):
        convert('10:15 AM to 5: PM')


def test_omit_to():
    with pytest.raises(ValueError):
        convert('11:55 AM - 6:40 PM')
