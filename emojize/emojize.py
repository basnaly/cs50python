import emoji

def main():
    while True:
        list = input('Input: ').split(' ')
        if len(list) == 1:
            print(f'Output: {emoji.emojize(list[0])}')
            break
        else:
            for string in list:
                index = string.find(':')
                print(index)

        # try:
        #     if len(list) == 1:
        #         print(f'Output: {emoji.emojize(user_input)}')

        # except ValueError:
        #     break


main()
