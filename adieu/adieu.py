import inflect

p = inflect.engine()
list = []

def main():
    while True:
        name = input('Name: ')
        try:
            # list.append(name)
            list = p.join((name), final_sep="")
            print(list)

        except EOFError:
            break



# "Adieu", "adieu", "to"


main()
