import inflect

p = inflect.engine()
list = []

while True:
    try:
        name = input('Name: ')
        list = p.join("Adieu", "adieu", "to")
        continue
    except EOFError:
        break


print(list)

