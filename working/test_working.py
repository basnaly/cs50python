from working import convert


def test_correct_version():
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'


def test_incorrect_version():
    assert convert('9:60 AM to 5:60 PM')
