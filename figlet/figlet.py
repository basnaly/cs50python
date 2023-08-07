from sys import argv
from pyfiglet import Figlet
from random import randint
import sys


def main():

    figlet = Figlet()

    fonts = figlet.getFonts()

    if len(argv) != 1 and len(argv) != 3
    and (argv[1] == "-f" or argv[1] == "--font") and argv[2].strip() in fonts:
        sys.exit("Invalid usage ")

    str = input("Input: ")

    try:
        if len(argv) == 1:
            index = randint(0, len(fonts))
            random_font = fonts[index]
            figlet.setFont(font=random_font)
            print("Output: ")
            print(figlet.renderText(str))
        elif len(argv) == 3:
            figlet.setFont(font=argv[2].strip())
            print("Output: ")
            print(figlet.renderText(str))
    except e:
        sys.exit(f"Error: {e}")


main()
