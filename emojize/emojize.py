import emoji

def main():
    list = input('Input: ').split(' ')
    if len(list) == 1:
        print(f"Output: {emoji.emojize(list[0], language='alias')}")

    else:
        print(f'Output: {list[0]} {emoji.emojize(list[1])}')



main()
