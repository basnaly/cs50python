def main():
    vowels = ['a', 'e', 'i', 'o','u']
    string = input('Input: ')
    for char in string:
        # Check if char is in the vowels list
        if char.lower() in vowels:
            string = string.replace(char, '')
    print(f'Output: {string}')


main()
