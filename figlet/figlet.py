from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts_list = figlet.getFonts()

str = input('Input: ')

if len(sys.argv) == 1:
    random_font = random.choices(figlet.getFonts())
    print(random_font)
    font = figlet.renderText(str)
    print(font)

elif len(sys.argv) == 3:
    if (sys.argv[1] != '-f' or sys.argv[1] != '--font') and sys.argv[2] not in fonts_list:
        sys.exit('Wrong arguments')
    else:
        my_font = sys.argv[2]
        updated_font = figlet.setFont(font=my_font)
        print(updated_font)

else:
    sys.exit('Wrong arguments')
