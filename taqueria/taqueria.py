

menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():

    sum = 0
    while True:
        try:
            if menu[key] in menu:
                item = input("Item: ")
                transformed = item.strip().lower().title()
                sum += menu[transformed]
                print("Total: $%.2f" % sum)
            else:
                continue
        except EOFError:
            break

main()