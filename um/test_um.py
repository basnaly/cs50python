from um import count
import pytest


def test_correct_argument():
    assert count('today, um, is, cold, um') == 2


def test_yum_argument():
    assert count('today, um, is, cold, yum') == 1


def test_dots_argument():
    assert count('um...') == 1


def test_uppercase_argument():
    assert count('boundary, Um, helps, ums, to, uM, limit' ) == 2
