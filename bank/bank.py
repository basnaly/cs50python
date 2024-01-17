def main():
    greet = input('Greeting: ').strip().casefold().split(',')
    print(greet)

    if greet[0] == 'hello':
        print('$0')
    elif greet[0] == 'h':
        print('$20')
    else:
        print('$100')


main()

