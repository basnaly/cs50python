import inflect

p = inflect.engine()
# list = ["Adieu", "adieu", "to"]

while True:
    try:
        name = input('Name: ')
        list = p.join(("Adieu", "adieu", "to", name))
        print(list)
        continue
    except EOFError:
        break




