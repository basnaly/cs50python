import re

# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>


def main():
    print(parse(input("HTML: ")))


def parse(s):

    address = 'https://youtu.be/'

    string = re.search(r'^(?:.+)(?:https?://(?:www\.)?)(?:youtube\.com/)(?:embed/)([a-zA-Z0-9]+)(?:.+)$', s)
    if string is None:
        return None
    return address + string.group(1)


if __name__ == "__main__":
    main()
