import inflect

p = inflect.engine()
list = ["Adieu", "adieu", "to"]

while True:
    try:
        name = input('Name: ')
        l = p.join((name for name in list))
        print(l)
        continue
    except EOFError:
        break




