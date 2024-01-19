def main():
    # vowels = [a, e, i, o, u]
    string = input('Input: ')
    for char in string:
        if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
            string = string.replace(char, '')
    print(f'Output: {string}')


main()
