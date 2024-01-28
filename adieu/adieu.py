import inflect

p = inflect.engine()
names = []

def main():
    while True:
        name = input('Name: ')
        try:
            list.append(name)
            l = p.join((list), final_sep="")
            print(l)

        except EOFError:
            break



# "Adieu", "adieu", "to"


main()
