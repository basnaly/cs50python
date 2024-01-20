def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if all chars are alphabetic and numeric only
    if s.isalnum() == False:
        return False

    # Check if 2 first chars are alphabetic
    if s[0:2].isalpha() == False:
        return False

    first_digit = None
    i = 0
    # Find the first digit and its index
    for c in s:
        if c.isdigit():
            first_digit = c
            break
        i += 1

    # Check if the first digit = 0
    if first_digit == '0':
        return False

    # Check if between first_digit and end of string there are numbers only
    if first_digit and s[i:].isdigit() == False:
        return False

    # Count letters in string
    letter_counter = 0
    for c in s:
        if c.isalpha() == True:
            letter_counter += 1

    # Check if number of letters less than 2 or more than 6
    if letter_counter < 2 or letter_counter > 6:
        return False

    return True


main()
