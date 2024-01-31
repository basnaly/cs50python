from plates import is_valid

def test_correct_argument():
    assert is_valid('star50') == True

def test_punctuation_argument():
    assert is_valid('CS50:') == False

def test_length_argument():
    assert is_valid('Harvard') == False

def test_number_placement():
    assert is_valid('cs50p') == False

def test_zero_placement():
    assert is_valid('cs05') == False

def test_numeric_placement():
    assert is_valid('50') == False
