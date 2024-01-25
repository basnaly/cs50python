import emoji

def main():
    while True:
        list = input('Input: ').split(' ')
        if len(list) == 1:
            print(f'Output: {emoji.emojize(list[0])}')
            break
        else:
            print(f'Output: {list[0]} {emoji.emojize(list[1])}')

        # try:
        #     if len(list) == 1:
        #         print(f'Output: {emoji.emojize(user_input)}')

        # except ValueError:
        #     break


main()
