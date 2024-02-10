import re
import sys


# https://youtu.be/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))


def parse(s):

    # url = re.search(r"^https?://(?:www\.)youtu.be[^\.com/embed]/(.+)$", s)

    url = re.search(r"^(https?://)$", s)
    return url.group(0)


if __name__ == "__main__":
    main()
