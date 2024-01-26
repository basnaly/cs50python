import emoji

def main():
    # Save user's input into str
    str = input('Input: ')
    # From: https://pypi.org/project/emoji/
    print(f'Output: {emoji.emojize(str, language="alias")}')


main()
