def main():
    greet = input('Greeting: ').strip().casefold().split(',')
    get_money = value(greet)
    print(f'${get_money}')



def value(greeting):

    # Check the first word in the sentence (if exists)
    if greeting[0] == 'hello':
        return 0
    # Check the first letter in the first word of the sentence
    elif greeting[0][0] == 'h':
        return 20
    else:
        return 100


if __name__ == '__main__':
    main()
