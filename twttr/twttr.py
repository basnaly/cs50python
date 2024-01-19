def main():
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = input('Input: ').casefold()
    for char in string:
        if char in vowels:
            string = string.replace(char, '')
        if char.isupper():
            string = string.replace(char, char.upper())
    print(f'Output: {string}')


main()
