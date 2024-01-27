import inflect

p = inflect.engine()


while True:
    list = ["Adieu", "adieu", "to"]
    try:
        name = input('Name: ')
        list.append(name)
        l = p.join((list), final_sep="")
        print(l)
        continue
    except EOFError:
        break



