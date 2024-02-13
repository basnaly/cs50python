import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    try:
        hour = r'[0-9]|1[0-9]|2[0-4]'
        minutes = r'[0-5][0-9]'
        format = r' [A|P]M'

        data = re.search(fr'^({hour})(:{minutes})?({format})(?: to )({hour})(:{minutes})?({format})?$', s)
        start_hour, start_minutes, start_format, end_hour, end_minutes, end_format = data.groups(':00')
        # print(start_hour, start_minutes, start_format, end_hour, end_minutes, end_format)

        # Check start time
        if start_format.lstrip() == 'AM' and int(start_hour) < 10:
            start_time = '0' + start_hour + start_minutes

        elif start_format.lstrip() == 'AM':
            start_time = start_hour + start_minutes

        if start_format.lstrip() == 'AM' and int(start_hour) == 12:
            start_time = '00' + start_minutes

        if start_format.lstrip() == 'PM':
            start_time = str(int(start_hour) + 12) + start_minutes

        if start_format.lstrip() == 'PM' and int(start_hour) == 12:
            start_time = '12' + start_minutes

        # Check end time
        if end_format.lstrip() == 'AM' and int(end_hour) < 10:
            end_time = '0' + end_hour + end_minutes

        elif end_format.lstrip() == 'AM':
            end_time = end_hour + end_minutes

        if end_format.lstrip() == 'AM' and int(end_hour) == 12:
            end_time = '00' + end_minutes

        if end_format.lstrip() == 'PM':
            end_time = str(int(end_hour) + 12) + end_minutes

        if end_format.lstrip() == 'PM' and int(end_hour) == 12:
            end_time = '12' + end_minutes

        return start_time + ' to ' + end_time

    except:
        raise ValueError


if __name__ == "__main__":
    main()

