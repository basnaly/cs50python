def main():
    greet = input('Greeting: ').strip().casefold()


    if greet == 'hello':
        print('$0')
    elif greet[0] == 'h':
        print('$20')
    else:
        print('$100')


main()

