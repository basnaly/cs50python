def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    is_chars_numbers = s.isalnum()
    is_chars = s[0:2].isalpha():
    count = 0
    for c in s:
        if c.isalpha():
            count = count + 1
    if 2 < count <= 6
    



main()
