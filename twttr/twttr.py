def main():
    word = input('Input: ')
    shorten(word)
    print(f'Output: {word}')


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in word:
        # Check if char is in the vowels list
        if char.lower() in vowels:
            return word.replace(char, '')


if __name__ == '__main__':
    main()
