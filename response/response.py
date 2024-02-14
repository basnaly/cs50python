from validator_collection import validators, checkers, errors
import validators


def main():

    email = input("What's your email address? ")

    is_valid = validators.email()
    if is_valid:
        print('Valid')
    else:
        print('Invalid')


main()
