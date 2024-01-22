def main():

    while True:
        formatted_fraction = input('Fraction: ')
        try:
            # C
            fraction = formatted_fraction.split('/')
            if fraction[0].isdecimal() == False or fraction[1].isdecimal() == False:
                continue
            if int(fraction[0]) > int(fraction[1]):
                continue
            if fraction[0] == '0':
                print('E')
                return
            if fraction[0] == fraction[1]:
                print('F')
                return

            result = round(float(fraction[0]) / float(fraction[1]) * 100)
            if result <= 1:
                print('E')
            elif result >= 99:
                print('F')
            else:
                print(f'{int(result)}%')
            return
        except ValueError:
            pass
        except ZeroDivisionError:
            return

main()
