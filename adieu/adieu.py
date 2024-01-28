import inflect

p = inflect.engine()
names = []

def main():
    while True:
        name = input('Name: ')
        try:
            names.append(name)
            list = p.join((names), final_sep="")
            print(f'Adieu, adieu, to {list}')

        except EOFError:
            break


main()
