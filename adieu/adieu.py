import inflect

p = inflect.engine()
# Create list of names
names = []

def main():
    while True:
        try:
            name = input()
            # Add name to the names list
            names.append(name)


        except EOFError:
            break

    list = p.join((names))
    print(f'Adieu, adieu, to {list}')

main()
