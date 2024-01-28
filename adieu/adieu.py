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
            print(f'Adieu, adieu, to {list}')
            continue
        
        except EOFError:
            break

main()
