import re
import sys


def nain():
    print(validate(input('IPv4 Address: ')))


def validate(ip):

    # 0-199: [0-1]?[0-9]?[0-9]?
    # 200-249 2[0-4][0-9]
    # 250-255 25[0-5]

    regex_pattern =




if __name__ == '__main__':
    main()
