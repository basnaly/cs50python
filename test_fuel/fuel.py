def main():
    fraction = input('Fraction: ')
    percentage = convert(fraction)
    result = gauge(percentage)
    print(f'{result}')

def convert(fraction):
    while True:
        try:
            # Split user's input by '/' and get list
            fraction = fraction.split('/')
            if fraction[0].isdecimal() == False or fraction[1].isdecimal() == False:
                continue
            if int(fraction[0]) > int(fraction[1]):
                continue
            if fraction[0] == '0':
                return 'E'
            if fraction[0] == fraction[1]:
                return 'F'

            # Calculate percent:
            percentage = round(float(fraction[0]) / float(fraction[1]) * 100)
            return percentage

        except ValueError:
            pass
        except ZeroDivisionError:
            return


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return percentage + '%'


if __name__ == '__main__':
    main()
