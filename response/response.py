from validator_collection import validators
import validators


def main():

    email_address = input("What's your email address? ")

    is_valid = validators.email(email_address)
    if is_valid:
        print('Valid')
    else:
        print('Invalid')


main()
