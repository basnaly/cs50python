import emoji

def main():
    while True:
        list = input('Input: ').split(' ')
        try:
            if len(list) == 1:
                print(f'Output: {emoji.emojize(user_input)}')
            else:
                for item in list:
                    
    user_text = user_input[0]
    user_emoji = user_input[1]

    #print(emoji.emojize(':camel:'))


main()
