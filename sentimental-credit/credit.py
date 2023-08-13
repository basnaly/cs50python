# TODO

from cs50 import get_int, get_string
import re

# American Express uses 15-digit numbers
    amex_digits = 15;
# MasterCard uses 16-digit numbers,
    master_digits = 16;
# Visa uses 13- and 16-digit numbers
    visa_digits1 = 13;
    visa_digits2 = 16;

amex_start1 = 34;
amex_start2 = 37;
master_start1 = 51;
master_start2 = 52;
master_start3 = 53;
master_start4 = 54;
master_start5 = 55;
visa_start = 4;

while True:
    card_number = get_string("Number ")
    if card_number > 0:
        break

pattern_amex = re.search("^34|37")

if len((card_number) != 13 or len(card_number) != 15 or len(card_number) != 16)
    print("INVALID")
if
