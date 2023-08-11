

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
            item = input("Item: ")
            if item not in menu:
                continue
            else:
                transformed = item.strip().lower().title()
                sum += menu[transformed]
                print("Total: $%.2f" % sum)
        except EOFError:
            break

main()