import inflect

p = inflect.engine()
list = ["Adieu", "adieu", "to"]

while True:

    try:
        name = input('Name: ')
        list.append(name)
        list = p.join((list), final_sep="")

        continue
    except EOFError:
        break

 print(list)

