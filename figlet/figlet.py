from pyfiglet import Figlet
import random
import sys

figlet = Figlet()
fonts_list = figlet.getFonts()
print(fonts_list)

str = input('Input: ')

if len(sys.argv) == 1:
    random_font = random.choices(figlet.getFonts())
    print(random_font)
    font = figlet.renderText(str)
    print(font)

elif len(sys.argv) == 3:
    font_name = argv[2]
    if (argv[1] != '-f' or argv[1] != '--font') and argv[2] != name:
        sys.exit('Wrong arguments')

    # set_font = figlet.setFont(font=random_font)

else:
    sys.exit('Wrong arguments')
