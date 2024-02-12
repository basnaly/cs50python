import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        # 24: 2[0-4] 1[0-9] [0-9]
        hours = r'2[0-4]|1[0-9]|[0-9]'
        minutes = r'[0-59]'

        a = re.search(fr'^({hours})(:{minutes})$', s)
        # start_hour, start_minutes
        # print(start_hour, start_minutes)
        print(a.group(1))

    except:
        raise ValueError


if __name__ == "__main__":
    main()

