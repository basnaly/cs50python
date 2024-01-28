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
    ...


if __name__ == "__main__":
    main()
