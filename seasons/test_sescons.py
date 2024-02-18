from datetime import date
import inflect


def main():
    minutes = get_minutes(input('Date of Birth: '))

    p = inflect.engine()
    result = p.number_to_words(minutes).capitalize()
    print(f'{result} minutes.')


def get_minutes():


main()
