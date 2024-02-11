import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        data = s.split(' ')
        # ['9:00', 'AM', 'to', '5:00', 'PM']
        print(data[0])

    except ValueError:
        sys.exit('Value error')




if __name__ == "__main__":
    main()

