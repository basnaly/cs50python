from datetime import date, datetime
import inflect


def main():
    minutes = get_minutes()

    p = inflect.engine()
    # result = p.number_to_words(minutes).capitalize()
    # print(f'{result} minutes.')


def get_minutes():

    try:

        today = date.today()
        bithday = input('Date of Birth: ')
        year, month, day = bithday.split('-')
        bithday_date = date(int(year), int(month), int(day))
        print(bithday_date)

        sub = today - bithday_date
        print(sub)

    except

main()

