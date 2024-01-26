import emoji

def main():
    # Save user's
    str = input('Input: ')
    print(f'Output: {emoji.emojize(str, language="alias")}')


main()
