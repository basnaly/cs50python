from numb3rs import validate


def test_correct_ip():
    assert validate('1.2.255.120') == True


def test_incorrect_ip():
    assert validate('3.120.256.128') == False
