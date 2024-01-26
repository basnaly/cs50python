import emoji

def main():

    str = input('Input: ')
    print(f'Output: {emoji.emojize(str, language='alias')}')


main()
