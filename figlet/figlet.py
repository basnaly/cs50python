from sys import argv
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

str = input("Input: ")

if len(argv) == 0:

    print("Output: " figlet.renderText(str))
elif len(argv) == 2:
    figlet.setFont(font=f) || figlet.setFont(font=font)
    print("Output: " figlet.renderText(s))
else:
    sys.exit