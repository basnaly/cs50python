import emoji

def main():
    while True:
        list = input('Input: ').split(' ')
        print(list)
        index = list.index(':')
        print(index)
        try:
            if len(list) == 1:
                print(f'Output: {emoji.emojize(user_input)}')

        except ValueError:
            break


main()
