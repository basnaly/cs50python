def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    is_letters = s[0:2].isalpha():

    is_letters_numbers = s.isalnum()


main()
