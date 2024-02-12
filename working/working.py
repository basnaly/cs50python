import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:

        # 9:00 AM to 5:00 PM
        # 24: 2[0-4] 1[0-9] [0-9]
        hours = r'2[0-4]|1[0-9]|[0-9]'
        minutes = r'[0-59]'

        data = re.search(fr'^({hours}+)(:{minutes}+)( AM)(?: to )({hours}+)(:{minutes}+)( PM+)$', s)
        start_hour, start_minutes, am, end_hour, end_minutes, pm = data.groups()
        print(start_hour, start_minutes, am, end_hour, end_minutes, pm)

        if am == 'AM':
            

    except:
        raise ValueError


if __name__ == "__main__":
    main()

