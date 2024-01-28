import random

def main():

    # random_number = None

    while True:

        level = input('Level: ')
        if level.isdecimal() == False:
            continue
        elif int(level) < 1:
            continue
        else:
            random_number = random.randint(1, int(level))
            break

    while True:

        guess = input('Guess: ')

        if guess.isdecimal() == False:
            continue
        guess = int(guess)
        if guess < 0:
            continue
        elif guess < random_number:
            print('Too small!')
        elif guess > random_number:
            print('Too large!')
        print('Just right!')
        break


main()
