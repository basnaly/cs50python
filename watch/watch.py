import re
import sys


# https://youtu.be/xvFZjo5PgG0
# http://youtube.com/embed/xvFZjo5PgG0


def main():
    print(parse(input("HTML: ")))


def parse(s):

    string = 'https://youtu.be/'
    a = re.search(r'^(?:.+src=")(?:https?://)(?:www\.youtube\.com/)(?:embed)/([a-zA-Z0-9]+)(?:".+)$', s)
    if a is None:
        return None
    return string + a.group(1)


if __name__ == "__main__":
    main()
