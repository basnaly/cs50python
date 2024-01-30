def main():
    greet = input('Greeting: ')
    get_money = value(greet)
    print(f'${get_money}')


def value(greeting):

    greet = greeting.strip().casefold().split(',')
    # Check the first word in the sentence (if exists)
    if greet[0] == 'hello':
        return 0
    # Check the first letter in the first word of the sentence
    elif greet[0][0] == 'h':
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
