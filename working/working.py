import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        m_time, am, to, e_time, pm = = s.split(' ')
        # ['9:00', 'AM', 'to', '5:00', 'PM']
        # print(m_time[0])
        if m_time[0] > 12 or e_time[0] > 12


    except ValueError:
        sys.exit('Value error')




if __name__ == "__main__":
    main()

