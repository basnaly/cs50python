from pyfiglet import Figlet
from sys import argv


def main():

    figlet = Figlet()

    if (argv[1] != "-f" or argv[1] !=["--font"]) and argv[2] != nameOfFont:
        sys.exit(1)


    figlet.getFonts()