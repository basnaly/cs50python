def main():
    greet = input('Greeting: ').strip().casefold().split(',')

    # Check the first word in the sentence (if exists)
    if greet[0] == 'hello':
        print('$0')
    # Check the first letter in the first word of the sentence
    elif greet[0][0] == 'h':
        print('$20')
    else:
        print('$100')


def value(greeting):


if __name__ == '__main__':
    main()
