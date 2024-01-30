def main():
    get_money = value(amount)
    print(f'${get_money}')


def value(greeting):

    amount = None
    greet = input('Greeting: ').strip().casefold().split(',')
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
