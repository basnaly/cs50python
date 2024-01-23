MENU = {
    "Baja Taco": 4.25,
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
    total = 0
    while True:
        try:
            # Convert user's input to insensitively case with words start with uppercase chars
            item = input('Item: ').casefold().title()
            if item in MENU:
                total += MENU[item]
                # Print total sum formatted to 2 decimal places
                print(f'Total: ${total:.2f}')
                continue
            elif item =='':
                return
            else:
                continue
        except EOFError:
            break


main()
