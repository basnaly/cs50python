import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:

        # 9:00 AM to 5:00 PM
        # 09:00 AM to 5:00 PM
        # 24: 2[0-4] 1[0-9] [0-9]
        hours = r'2[0-4]|1[0-9]|[0-9]'
        minutes = r'[0-59]'

        data = re.search(fr'^({hours}+)(:{minutes}+)( AM)(?: to )({hours}+)(:{minutes}+)( PM+)$', s)
        start_hour, start_minutes, am, end_hour, end_minutes, pm = data.groups()
        # print(start_hour, start_minutes, am, end_hour, end_minutes, pm)
        # 9 :00  AM 5 :00  PM

        start_time = start_hour + start_minutes
        end_time = end_hour + end_minutes

        print(am, start_hour)
        if am.lstrip() == 'AM' and int(start_hour) < 10:
            start_time = '0' + start_hour + start_minutes
        print(start_time)

        if 

    except:
        raise ValueError


if __name__ == "__main__":
    main()

