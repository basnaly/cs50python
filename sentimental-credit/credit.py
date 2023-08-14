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

def check_card(card_number):
    # sum = 0
    # i = 0
    # while (int(card_number) > 0):
    #     rem = int(card_number) % 10
    #     card_number = (int(card_number) - rem) / 10
    #     if i % 2 == 0:
    #         # print(rem)
    #         sum = sum + rem
    #     else:
    #         doubled = rem * 2
    #         if doubled > 9:
    #             doubled = 1 + (doubled - 10)
    #         sum = sum + doubled
    #     i += 1
    #     # print(sum)

    sum = 0
    reverse_number = card_number[::-1]
    for i in range(len(card_number)):
        if len(reverse_number) % 2 == 0:
            sum = sum + int(reverse_number[i])
        else:
            doubled = reverse_number[i] * 2
            if doubled > 9:
                doubled = 1 + (doubled - 10)
            sum = sum + doubled

        print(sum)
    return sum

def is_valid(sum):
    if sum % 10 == 0:
        return True
    return False

while True:
    card_number = get_string("Number: ")
    if int(card_number) > 0:
        break

sum = check_card(card_number)

pattern_amex = re.search("^34|^37", card_number)
pattern_master = re.search("^51|^52|^53|^54|^55", card_number)
pattern_visa = re.search("^4", card_number)

if pattern_amex and len(card_number) == 15 and is_valid(sum):
    print("AMEX")
elif pattern_master and len(card_number) == 16 and is_valid(sum):
    print("MASTERCARD")
elif pattern_visa and len(card_number) in visa_digits and is_valid(sum):
    print("VISA")
else:
    print("INVALID")
