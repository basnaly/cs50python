def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s.isalnum() == False:
        break
    if s[0:2].isalpha() == False:
        break
    if s[3:-2].isdigital = False:
        break
    count = 0
    for c in s:
        if c.isalpha():
            count = count + 1
    if 2 > count > 6:
        break
    else:
        return True


main()
