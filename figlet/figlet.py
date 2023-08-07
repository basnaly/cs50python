from sys import argv
from pyfiglet import Figlet

figlet = Figlet()

figlet.getFonts()

if len(argv) == 0:

    print(figlet.renderText(s))
elif len(argv) == 2:
    figlet.setFont(font=f) || figlet.setFont(font=font)
    print(figlet.renderText(s))
else:
