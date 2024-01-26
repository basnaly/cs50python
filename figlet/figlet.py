from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts_list = figlet.getFonts()

if len(sys.argv) == 1:
    str = input('Input: ')
    random_font = random.choices(figlet.getFonts())
    print(random_font)
    print(figlet.renderText(str))

elif len(sys.argv) == 3:
    if (sys.argv[1] != '-f' or sys.argv[1] != '--font') and sys.argv[2] not in fonts_list:
        sys.exit('Invalid usage')
    else:
        str = input('Input: ')
        my_font = sys.argv[2]
        updated_font = figlet.setFont(font=my_font)
        print(figlet.renderText(str))

else:
    sys.exit('Invalid usage')
