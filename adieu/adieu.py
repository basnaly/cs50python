import inflect

p = inflect.engine()
list = []

while True:

    try:
        name = input('Name: ')
        list.append(name)
        l = p.join((list), final_sep="")
        print("asd "+l)
        continue
    except EOFError:
        break

# "Adieu", "adieu", "to"
