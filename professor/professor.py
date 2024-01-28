import random


def main():
    level = get_level()


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
    i = 0
    j = 0
    score = 0

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

        pattern = input(x + y + ' = ')
        


if __name__ == "__main__":
    main()
