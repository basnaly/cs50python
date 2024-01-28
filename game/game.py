import random

def main():

    # random_number = None

    while True:

        level = input('Level: ')
        if  and level.isdecimal == False:
            continue
        else:
            random_number = random.randint(1, int(level))
            break

    while True:

        guess = int(input('Guess: '))
        if guess < 1:
            continue
        elif guess < random_number:
            print('Too small!')
        elif guess > random_number:
            print('Too large!')
        else:
            print('Just right!')
            break


main()
