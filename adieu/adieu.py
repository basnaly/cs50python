import inflect

p = inflect.engine()
list = ["Adieu", "adieu", "to"]

while True:
    try:
        name = input('Name: ')
        list = p.join(('anc'), final_sep="")
        print(list)
        continue
    except EOFError:
        break




