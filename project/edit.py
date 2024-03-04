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

            total = 0
            for item in table:
                total += round(float(item['Sum $']), 2)

            print(tabulate(table, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(table)]))
            cprint(f'Total: ${total}\n', attrs=['bold'])

    except FileNotFoundError:
        sys.exit('File does not exist')

    while True:
        try:
            cprint('What would you like to edit?', 'blue', attrs=['bold'])
            cprint('Your options are:', 'blue')
            cprint('1. To add new one type: "1".', 'blue')
            cprint('2. To delete type: "2 <x>", where x is the number of the product in the cart.', 'blue')
            cprint('3. To change quantity type: "3 <x> <y>" where x is the number of the product and y is a new amount.', 'blue')
            cprint('4. To exit and save use Ctrl-D.', 'blue')

            choice = input('Your choice: ').split(' ')

            if choice[0] == '1':
                add(table)

            elif choice[0] == '2' and 0 < int(choice[1]) <= len(table):
                delete(table, int(choice[1]) - 1)

            elif choice[0] == '3':
                change_quantity(table, int(choice[1]) - 1, float(choice[2]))

            else:
                continue

            total = 0
            for item in table:
                total += round(float(item['Sum $']), 2)

            print(tabulate(table, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(table)]))
            cprint(f'Total: ${total}\n', attrs=['bold'])

        except ValueError as e:
            print(e)
            continue

        except EOFError:
            save_to_cart(table)
            cprint('\nRun `python project.py -m edit` to edit the order.', 'blue')
            cprint('Run `python project.py -m finish` to complete the order.', 'blue')
            break


def add(table):
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["Name"]} {item["Icon"]} {item["Price/Kg"]}')

    try:
        current_product = Product.get_product()
        # Check if the current product is already in the cart
        exists_products = [product['Name'] for product in table]
        if current_product.name in exists_products:
            cprint(f'You already have {current_product.name} in your cart!', 'blue')
            cprint('To change quantity type: "3 <x> <y>" where x is the number of the product and y is a new amount.', 'blue')

        current_product.set_quantity_sum()
        table.append(current_product.get_product_obj())

    except ValueError as e:
        print(e)


def delete(table, index):
    table.pop(index)


def change_quantity(table, index, new_quantity):
    table[index]['Quantity'] = new_quantity
    table[index]['Sum $'] = round(float(table[index]['Quantity']) * float(table[index]['Price/Kg']), 2)


def save_to_cart(table):
    csv_file = 'cart.csv'
    with open(csv_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price/Kg', 'Quantity', 'Sum $'])
        writer.writeheader()
        for row in table:
            writer.writerow(row)
