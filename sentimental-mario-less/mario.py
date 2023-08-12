# TODO

from cs50 import get_int

while True:

    number = get_int("Height: ")

    if (0 < number < 9):
        break

for i in range(number):
    print(" " * (number - 1), "#" * number,)

