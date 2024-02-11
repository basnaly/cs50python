import re


def main():
    print(parse(input("HTML: ")))


def parse(s):

    address = 'https://youtu.be/'
    str = re.search(r'^@', s)
    if str is None:
        return None
    return url


if __name__ == "__main__":
    main()
