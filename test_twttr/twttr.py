def main():
    word = input('Input: ')
    string = shorten(word)
    print(f'Output: {string}')


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        # Check if char is in the vowels list
        if char.lower() in vowels:
            word = word.replace(char, '')
    return word

if __name__ == '__main__':
    main()