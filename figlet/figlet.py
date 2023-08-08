from pyfiglet import Figlet
from sys import argv, exit
import random


def main():

    figlet = Figlet()
    fonts = figlet.getFonts()

    if len(argv) == 1:
        random_index = random.randrange(0, len(fonts))
        random_font_name = fonts[random_index]
        figlet.setFont(font=random_font_name)

    elif len(argv) == 3:
        if argv[1] != "-f" and argv[1] != "--font":
            exit("Invalid usage")

        elif argv[2] not in fonts:
            exit("Invalid usage")

        else:
            figlet.setFont(font=argv[2])

    else:
        exit("Error")

    string = input("Input: ")
    print("Output: ")
    print(figlet.renderText(string))

main()