def main():
    greet = input('Greeting: ')
    get_money = value(greet)
    print(f'${get_money}')


def value(greeting):

    greet = greeting.strip().casefold().split(',')
    # Check the first word in the sentence (if exists)
    if greet[0] == 'hello':
        amount = 0
    # Check the first letter in the first word of the sentence
    elif greet[0][0] == 'h':
        amount = 20
    else:
        amount = 100
    return amount


if __name__ == '__main__':
    main()
