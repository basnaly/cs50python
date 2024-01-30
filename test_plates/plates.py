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

    # Check if number of chars in the string less than 2 or more than 6
    if len(s) < 2 or len(s) > 6:
        return False

    # Check if 2 first chars are alphabetic
    if s[0:2].isalpha() == False:
        return False

    # Find the first digit and its index
    first_digit = None
    i = 0
    for c in s:
        i += 1
        if c.isdigit():
            first_digit = c
            break

    # Check if the first digit = 0
    if first_digit == '0':
        return False

    # Check if string has alphabetic chars only and lengh of the string more or equal than 2 and less or equal than 6
    if first_digit == None and 2 <= len(s) <= 6:
        return True

    # Check if between first_digit and end of string there are numbers only
    if s[i:].isdigit() == False:
        return False

    return True


if __name__ == '__main__':
    main()
