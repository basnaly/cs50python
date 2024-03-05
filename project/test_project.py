from project import main


def test_create_argument():
    assert main([h] [-m MODE]) == True
