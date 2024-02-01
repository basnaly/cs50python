import pytest
from fuel import convert, gauge

def test_corrected_argument():
    assert convert('1/2') == 50
