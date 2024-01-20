def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s.isalnum() == False:
        return False
    if s[0:2].isalpha() == False:
        return False
    if s[-1].isalpha() == True:
        return False
    count = 0
    for c in s:
        if c.isalpha():
            count = count + 1
    print(count)
    if count < 2 or count > 6:
        return False
    else:
        return True


main()
