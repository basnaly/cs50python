import re
import sys


def main():
    print(validate(input('IPv4 Address: ')))


def validate(ip):

    # 0-199: [0-1]?[0-9]?[0-9]?
    # 200-249 2[0-4][0-9]
    # 250-255 25[0-5]

    regex_pattern = r'(25[0-5] | 2[0-4][0-9] | [01]?[0-9]?[0-9]?)'

    if re.search(f"^{regex_pattern}\.{regex_pattern}\.{regex_pattern}\.{regex_pattern}$", ip):
        return True
    return False





if __name__ == '__main__':
    main()
