import inflect

p = inflect.engine()
list = ["Adieu", "adieu", "to"]

while True:
    try:
        name = input('Name: ')
        list = p.join(name)
        continue
    except EOFError:
        break


print(list)

