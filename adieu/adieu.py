import inflect

p = inflect.engine()
# Create list of names
names = []

def main():
    while True:
        try:
            name = input('Name: ')
            # Add name to the names list
            names.append(name)
            list = p.join((names), final_sep="")

            continue

        except EOFError:
            break

    print(f'Adieu, adieu, to {list}')

main()
