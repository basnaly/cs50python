import re


def main():
    print(parse(input("HTML: ")))


def parse(s):


    url = re.search(r'^@', s)
    if url is None:
        return None
    return url


if __name__ == "__main__":
    main()
