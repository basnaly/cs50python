import re

# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>


def main():
    print(parse(input("HTML: ")))


def parse(s):

    address = 'https://youtu.be/'

    a = re.search(r'^(?:.+src=")(?:https?://)(?:(?:www\.)?youtube\.com/)(?:embed/)([a-zA-Z0-9]+)(?:".+)$', s)

    a = re.search(r'^(?:.+src=")(?:https?://)(?:(?:www\.)?youtube\.com/)(?:embed/)([a-zA-Z0-9]+)(?:".+)@', s)
    if a is None:
        return None
    return address + a.group(1)


if __name__ == "__main__":
    main()
