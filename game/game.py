import random

def main():

    # random_number = None

    while True:

        level = int(input('Level: '))
        
        if level < 1 and level.isdecimal == False:
            continue
        else:
            random_number = random.randint(1, level)
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
