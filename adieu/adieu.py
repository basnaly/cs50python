import inflect

p = inflect.engine()
list = ["Adieu", "adieu", "to"]

while True:
    try:
        name = input('Name: ')
        continue
    except EOFError:
        break

list = p.join(name)
print(list)

