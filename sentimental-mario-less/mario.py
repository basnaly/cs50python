# TODO

from cs50 import get_int

while True:
    number = get_int("Height: ")
    if 1 < number < 8:
        break

for i in range(number):
    print(" " + (number - i - 1) + "#")
