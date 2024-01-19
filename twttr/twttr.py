def main():
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    string = input('Input: ')
    for char in string:
        # Check if char is in the vowels list
        if char in vowels:
            string = string.replace(char, '')
        # Check if char is in an uppercase in the string
        if char.isupper():
            string = string.replace(char, char.upper())
    print(f'Output: {string}')


main()
