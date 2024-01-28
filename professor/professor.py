import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        # Prompt user for level`
        level = input('Level: ')
        # Convert user's input into integer
        try:
            level = int(level)
        except ValueError:
            continue
        if level < 1 or level > 3:
            continue
        else:
            return level


def generate_integer(level):
    x = 0
    y = 0
    score = 0

    i = 0
    while i < 10:
        # Get random x and y
        if level == 1:
            x = random.randint(0, 9)
            y = random.randint(0, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)

        # Check wrong additon
        j = 0
        while j < 3:
            pattern = input(str(x) + ' + ' + str(y) + ' = ')
            sum = x + y
            # If addition was correct, add score
            if sum == int(pattern):
                score += 1
                break

            else:
                print('EEE')
                # If 3 tries were wrong, show correct answer
                if j == 2:
                    print(f'{x} + {y} = {sum}')
                j += 1
                continue

        i += 1
        continue

    # Print total scores
    print(f'Score: {score}')


if __name__ == "__main__":
    main()
