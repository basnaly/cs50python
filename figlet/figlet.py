from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

str = input('Input: ')

if len(sys.argv) == 1:
    font = random(figlet.getFonts(str))
    print(font)
