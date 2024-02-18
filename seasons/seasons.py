from datetime import date, timedelta
import inflect
import sys


def main():
    minutes = get_minutes(input('Date of Birth: '))

    p = inflect.engine()
    result = p.number_to_words(minutes).capitalize()
    print(f'{result} minutes.')


def get_minutes(bithday):

    try:
        today = date.today()

        year, month, day = bithday.split('-')
        # Transform bithday into date format
        bithday_date = date(int(year), int(month), int(day))

        # Calculate days between today and bithday
        days = today - bithday_date
        total_minutes = int(timedelta.total_seconds(days) / 60)
        return total_minutes

    except ValueError:
        sys.exit('Invalid date')


if __name__ == "__main__":
    main()

