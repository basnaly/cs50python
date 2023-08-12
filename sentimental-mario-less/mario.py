# TODO

from cs50 import get_int

number = get_int("Height: ")
if (number < 1 or number > 8):
    break
else:
    for i in range(number):
        print("#")
