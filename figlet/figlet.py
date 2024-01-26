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
    if (argv[1] != '-f' or argv[1] != '--font') and argv[2] not in fonts_list:
        sys.exit('Wrong arguments')
    else:
        updated_font = figlet.setFont(font=argv[2])
        print(updated_font)

else:
    sys.exit('Wrong arguments')
