import emoji

def main():
    while True:
        list = input('Input: ').split(' ')
        try:
            if len(list) == 1:
                print(f'Output: {emoji.emojize(user_input)}')
            else:
                index = list.index(':')
                print(index)
        except ValueError:
            continue


main()
