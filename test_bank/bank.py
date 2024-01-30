def main():
    get_money = value(greeting)
    print(f'${get_money}')


def value(greeting):
    print(greeting)

    greet = input('Greeting: ').strip().casefold().split(',')
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
