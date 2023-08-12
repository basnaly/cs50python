# TODO

from cs50 import get_int

while True:

    number = get_int("Height: ")

    if (number < 1 or number > 8):
        break

for i in range(number):
    print("#")
