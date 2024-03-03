import csv, sys
from tabulate import tabulate
from termcolor import colored, cprint
from product import FARM_LIST, Product


def edit():
    cprint('Here is your order:', 'blue')
    table = []
    try:
        csv_file = 'cart.csv'
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(table)]))

    except FileNotFoundError:
        sys.exit('File does not exist')

    while True:
        try:
            cprint('What would you like to edit?', 'blue', attrs=['bold'])
            cprint('To add new one type: "1".', 'blue')
            cprint('To delete type: "2 <x>", where x is the number of the product in the cart.', 'blue')
            cprint('To change quantity type: "3 <x> <y>" where x is the number of the product and y is a new amount.', 'blue')

            choice = input('Your choice: ').split(' ')

            if choice[0] == '1':
                add(table)

            elif choice[0] == '2' and 0 < int(choice[1]) <= len(table):
                delete(table, int(choice[1]) - 1)

            elif choice[0] == '3':
                change_quantity(table, int(choice[1]) - 1, int(choice[2]))

            else:
                continue

            print(tabulate(table, headers='keys', tablefmt='grid'))

        except ValueError as e:
            print(e)
            continue

        except EOFError:
            save_to_cart(table)
            break


def add(table):
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    try:
        current_product = Product.get_product()
        current_product.set_quantity_sum()
        table.append(current_product.get_product_obj())

    except ValueError as e:
        print(e)


def delete(table, index):
    table.pop(index)


def change_quantity(table, index, new_quantity):
    ffg


def save_to_cart(table):
    csv_file = 'cart.csv'
    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price/Kg', 'Quantity', 'Sum $'])
        writer.writeheader()
        for row in table:
            writer.writerow(row)
