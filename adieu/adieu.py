import inflect

p = inflect.engine()
list = ["Adieu", "adieu", "to"]

# while True:
#     try:
#         name = input('Name: ')
#         print(f"{p.join((name), final_sep='')}")

#         continue
#     except EOFError:
#         break

name = input('Name:')
list = p.join(name)
print(list)


