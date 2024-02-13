import re


def main():
    print(count(input("Text: ")))


def count(s):

    # Bound around the word 'um' in the pattern
    pattern = r'(\bum\b)'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)


if __name__ == "__main__":
    main()
