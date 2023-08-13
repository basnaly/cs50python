# TODO

from cs50 import get_string
import re

# American Express uses 15-digit numbers
# amex_digits = 15;
# MasterCard uses 16-digit numbers,
# master_digits = 16;
# Visa uses 13- and 16-digit numbers
visa_digits = [13, 16]

# amex_start1 = 34;
# amex_start2 = 37;
# master_start1 = 51;
# master_start2 = 52;
# master_start3 = 53;
# master_start4 = 54;
# master_start5 = 55;
# visa_start = 4;


def calc_sum(card_number):
    sum = 0
    for i in range(len(card_number)):
        rem = int(card_number) % 10
        card_number = (int(card_number) - rem) / 10
        if i % 2 == 0:
            sum = sum + rem
        else:
            doubled = rem * 2
            if doubled > 9:
                doubled = 1 + (doubled - 10)
            sum = sum + doubled
    return sum

def is_valid(sum):
    if sum % 10 == 0:
        return true
    return false


while True:
    card_number = get_string("Number: ")
    if int(card_number) > 0:
        break

pattern_amex = re.search("^34|^37", card_number)
pattern_master = re.search("^51|^52|^53|^54|^55", card_number)
pattern_visa = re.search("^3", card_number)

if len(card_number) == 15 and pattern_amex and is_valid:
    print("AMEX")
elif len(card_number) == 16 and pattern_master and is_valid:
    print("MASTER")
elif len(card_number) in visa_digits and pattern_visa and is_valid:
    print("VISA")
else:
    print("INVALID")

# 5105105105105100