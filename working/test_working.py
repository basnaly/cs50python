from working import convert
import pytest


def test_correct_version():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'


def test_incorrect_version():
    with pytest.raises(ValueError):
        convert('9:60 AM to 5:60 PM')


def test_omit_minutes():
    assert convert('9:20 AM 5:00 PM') == '09:20 to 17:00'
