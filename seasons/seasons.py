from datetime import date, datetime
import inflect


def main():
    minutes = get_minutes()

    p = inflect.engine()
    # result = p.number_to_words(minutes).capitalize()
    # print(f'{result} minutes.')


def get_minutes():

    today = date.today()
    # today_formated = datetime.strftime(today, '%Y-%m-%d')
    print(today)

    bithday = input('Date of Birth: ')
    bithday_formatted = 



main()

