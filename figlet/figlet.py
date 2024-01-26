from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) == 1:
    random(figlet.getFonts())
    print()
