def main():
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = input('Input: ')
    if string.isupper():
        for char in string:
            if char in vowels:
                string = string.replace(char, '')
        print(f'Output: {string}')


main()
