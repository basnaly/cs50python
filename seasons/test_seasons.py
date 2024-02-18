import pytest
from seasons import get_minutes


def test_correct_argument():
    assert get_minutes('1980-10-25') == 22782240


def test_incorrect_argument():
    with pytest.raises(SystemExit):
        get_minutes('April, 24 1995')
