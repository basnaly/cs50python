from sys import argv
from pyfiglet import Figlet
import sys


def main():

    figlet = Figlet()

    figlet.getFonts()

    str = input("Input: ")

    try:
        if len(argv) == 0:
            random.figlet.getFonts()
            print(f"Output:  {figlet.renderText(str)}")
        elif len(argv) == 2:
            pass
            # figlet.setFont(font=f) || figlet.setFont(font=font)
            # print("Output: " figlet.renderText(s))
    except:
        sys.exit("Error")


main()
