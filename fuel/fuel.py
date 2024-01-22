def main():

    while True:

        formatted_fraction = input('Fraction: ')
        if formatted_fraction = '4/4':
            print('F')
            return
        if formatted_fraction = '0/1':
            print('E')
            return
        else:
            try:
                fraction = formatted_fraction.split('/')
                if fraction[0].isdecimal() == False or fraction[1].isdecimal() == False:
                    return
                if int(fraction[0]) > int(fraction[1]):
                    return
                result = float(fraction[0]) / float(fraction[1]) * 100

