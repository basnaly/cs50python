def main():
    greet = input('Greeting: ').split(',')
    

    if greet == 'Hello':
        print('$0')
    elif greet[0] == 'h':
        print('$20')
    else:
        print('$100')


main()

