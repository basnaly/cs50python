import emoji

def main():

    string = input('Input: ')
    print(f"Output: {emoji.emojize(string ,language='alias')}")


main()
