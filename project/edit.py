import csv, sys
from tabulate import tabulate
from termcolor import colored, cprint
from product import FARM_LIST, Product


def edit():
    cprint('Here is your order:', 'blue')
    table = []
    try:
        csv_file = 'basket.csv'
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            index = 0
            for row in reader:
                row['Name'] = f'{index + 1}. ' + row["Name"]
                index += 1
                table.append(row)
            print(tabulate(table, headers='keys', tablefmt='grid'))


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
                print(choice[1])
                print('Selected delete')
                delete(table, choice[1])

            elif choice[0] == '3':
                print('Selected change quantity')

            else:
                continue

        except ValueError:
            continue



def add(table):
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    try:
        current_product = Product.get_product()
        current_product.set_quantity_sum()
        table.append(current_product.__dict__)
        print(table)

        print('Select another product or exit using Ctrl-D')

    except ValueError as e:
        print(e)

