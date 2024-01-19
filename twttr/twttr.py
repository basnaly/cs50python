def main():
    # vowels = [a, e, i, o, u]
    string = input('Input: ')
    for char in string:
        if char == 'a' and char == 'e' and char == 'i' and char == 'o' and char == 'u':
            string = string.replace(char, '')
        print(f'Output: {string}')



main()
