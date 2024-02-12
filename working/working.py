import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:

        # 9:00 AM to 5:00 PM
        # 09:00 AM to 5:00 PM

        # 24: 20->24: 2[0-4] 10->19: 1[0-9] 0->9: [0-9]
        # 59: 0->9: [0-9] 10->59: [15][09]
        hours = r'2[0-4]|1[0-9]|[0-9]'
        minutes = r'[0-5][0-9]'

        data = re.search(fr'^({hours})(:{minutes})?( [A|P]M)(?: to )({hours})(:{minutes})?( [A|P]M)$', s)
        start_hour, start_minutes, start_format, end_hour, end_minutes, end_format = data.groups(':00')
        # print(start_hour, start_minutes, am, end_hour, end_minutes, pm)
        # 9 :00  AM 5 :00  PM

        start_time = start_hour + start_minutes
        end_time = end_hour + end_minutes

        if start_format.lstrip() == 'AM' and int(start_hour) < 10:
            start_time = '0' + start_hour + start_minutes

        if start_format.lstrip() == 'AM' and (start_hour == '12:00' or start_hour == '12')
            start_time = '00:00'

        if start_format.lstrip() == 'PM':
            start_time = str(int(start_hour) + 12) + start_minutes

        if end_format.lstrip() == 'PM':
            end_time = str(int(end_hour) + 12) + end_minutes

        if end_format.lstrip() == 'AM' and int(end_hour) < 10:
            end_time = '0' + end_hour + end_minutes

        if end_format.lstrip() == 'PM' and (end_hour == '12:00' or end_hour == '12')
            end_time = '12:00'

        return start_time + ' to ' + end_time

    except:
        raise ValueError


if __name__ == "__main__":
    main()

