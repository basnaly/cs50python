# TODO

from cs50 import get_string
import re


def main():
    text = get_string("Text: ")

    letters = 0

    words = len(text.split(" "))

    sentences = len(re.split(r"\!|\.|\?", text)) - 1

    for i in range(len(text)):
        if text[i].isalpha():
            letters += 1

    index = round(
        0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8
    )

    if index < 1:
        print("Before Grade 1 ")
    elif index > 16:
        print("Grade 16+")
    else:
        print("Grade ", index)


main()
