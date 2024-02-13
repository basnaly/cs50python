from um import count
import pytest


def test_correct_argument():
    assert count('today, um, is, cold, um') == 2


def test_yum_argument():
    assert count('regex, um, is, not, easy, yum') == 1


def test_dots_argument():
    assert count('um...') == 1


def test_uppercase_argument():
    assert count('boundary, Um, between, two, uM, words') == 2
