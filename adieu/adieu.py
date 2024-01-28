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


        except EOFError:
            break

    list = p.join((names), final_sep="")
    print(f'\nAdieu, adieu, to {list}')

main()
