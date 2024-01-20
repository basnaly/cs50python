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
    if s[0:2].isalpha == False:
        returm False
    first_char = None
    i = 0
    # Check if the first char = 0
    for c in s:
        i += 1
        if c.isdigit():
            first_char == c
            break
    if first_char == 0:
        return False
    # Check if between first_char and last char there is letter
    if s[i:-1].is.digit == False:
        return False
    # 




main()
