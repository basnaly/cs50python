import random

while True:

    # Prompt user for level
    level = input('Level: ')
    # Check the user's input
    if level.isdecimal() == False:
        continue
    elif int(level) < 1:
        continue
    else:
        # Generate random number
        random_number = random.randint(1, int(level))
        break

while True:

    # Prompt user for guess
    guess = input('Guess: ')
    # Check the user's input
    if guess.isdecimal() == False:
        continue
    guess = int(guess)
    if guess < 0:
        continue
    elif guess < random_number:
        print('Too small!')
    elif guess > random_number:
        print('Too large!')
    else:
        print('Just right!')
        break

