# TODO

from cs50 import get_float

while True:
    value = get_float("Change owed: ")
    if value > 0:
        break

quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;
