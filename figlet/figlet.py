from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

str = input('Input: ')

if len(sys.argv) == 1:
    random_font = random.choices(figlet.getFonts())
    print(random_font)
    # font = figlet.renderText(str)
    # print(font)
