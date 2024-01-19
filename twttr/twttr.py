def main():
    vowels = ['a', 'e', 'i', 'o','u']
    string = input('Input: ')
    for char in string:
        # Check if char is in the vowels list
        if char.lower() in vowels:
            string = string.replace(char, '')
        # Check if char is in an uppercase in the string
        # if char.isupper():
        #     string = string.replace(char, char.upper())
    print(f'Output: {string}')


main()
