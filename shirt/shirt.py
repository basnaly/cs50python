import sys
from PIL import Image, ImageOps


def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    extentions = ['jpg', 'jpeg', 'png']
    name_input, extention_input = sys.argv[1].split('.')
    name_output, extention_output = sys.argv[2].split('.')

    if not extention_input.casefold() or extention_input not in extentions:
        sys.exit('Invalid input')
    elif not extention_output.casefold() or extention_output not in extentions:
        sys.exit('Invalid output')
    elif extention_input.casefold() != extention_output.casefold():
        sys.exit('Input and output have different extensions')

    try:
        shirt = Image.open('shirt.png')
        base_image = Image.open(sys.argv[1])
        size = shirt.size

        # Fit base_image according to the shirt
        base_image_fit = ImageOps.fit(base_image, size)
        # Paste shirt into the fit base image
        base_image_fit.paste(shirt, shirt)
        # Save fit base image with shirt into sys.argv[2] file
        base_image_fit.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit('Input does not exist')


main()
