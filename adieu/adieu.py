import inflect

p = inflect.engine()

names = []

def main():

    while True:
        try:
            # Prompt user for name
            name = input('Name: ')
            # Add name into names list
            names.append(name)
            continue
        except EOFError:
            break

    # Join names from names list to the str
    str = p.join((names))
    print(f'Adieu, adieu, to {str}')

main()
