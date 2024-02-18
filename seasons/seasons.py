from datetime import date, datetime, timedelta
import inflect
import sys


def main():
    minutes = get_minutes()
    print(minutes)

    p = inflect.engine()
    result = p.number_to_words(1234).capitalize()
    print(f'{result} minutes.')


def get_minutes():

    try:

        today = date.today()
        bithday = input('Date of Birth: ')
        year, month, day = bithday.split('-')
        bithday_date = date(int(year), int(month), int(day))
        print(bithday_date)

        days = today - bithday_date
        total_minutes = int(timedelta.total_seconds(days) / 60)
        print(total_minutes)
        # return total_minutes

    except ValueError:
        sys.exit('Invalid date')


main()

