def main():
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    string = input('Input: ')
    for char in string:
        if char in vowels:
            string = string.replace(char, '')
        if char.isupper():
            string = string.replace(char, char.upper())
    print(f'Output: {string}')


main()
