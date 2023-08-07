from sys import argv
from pyfiglet import Figlet
import sys


def main():

    figlet = Figlet()

    str = input("Input: ")
    print(figlet.getFonts())

    try:
        if len(argv) == 1:
            index = random.randint(0, len(figlet.getFonts()))
            random_font = figlet.getFonts()[index]
            figlet.setFont(font=random_font)
            print(f"Output:  {figlet.renderText(str)}")
        elif len(argv) == 3:
            pass
            # figlet.setFont(font=f) || figlet.setFont(font=font)
            # print("Output: " figlet.renderText(s))
    except e:
        sys.exit(f"Error: {e}")


main()
