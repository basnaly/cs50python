import random


def main():
    level = get_level()
    generate_integer(level)


def get_level():
    while True:
        level = input('Level: ')
        level = int(level)
        if 1 > level > 3:
            continue
        else:
            return level


def generate_integer(level):
    x = 0
    y = 0
    score = 0

    i = 0
    while i < 10:
        if level == 1:
            x = random.randint(1, 9)
            y = random.randint(1, 9)
        elif level == 2:
            x = random.randint(10, 99)
            y = random.randint(10, 99)
        elif level == 3:
            x = random.randint(100, 999)
            y = random.randint(100, 999)
        else:
            raise ValueError



        j = 0
        while j < 2:
            pattern = input(str(x) + ' + ' + str(y) + ' = ')
            sum = x + y
            if sum == int(pattern):
                score += 1
                break

            else:
                print('EEE')
                if j == 1:
                    print(f'{x} + {y} = {sum}')
                j += 1
                continue

        i += 1
        continue


if __name__ == "__main__":
    main()
