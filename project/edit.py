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
                row['Number'] = index
                index += 1
                table.append(row)
            print(tabulate(table, headers='keys', tablefmt='grid'))


    except FileNotFoundError:
        sys.exit('File does not exist')

    while True:

        try:
            cprint('What would you like to edit?', 'blue')
            cprint('To add new one type 1.', 'blue')
            cprint('To delete type 2, space and the number.', 'blue')
            cprint('To change quantity type 3, space, the number, space and the quantity you want to change to.', 'blue')

            choice = input('Your choice: ').split(' ')

            print(choice[1])

            if choice[0] == '1':
                add(table)

            elif choice[0] == '2' :
                print('Selected delete')

            elif choice[0] == '3' and choice[1].casefold()  == item_name:
                print('Selected change quantity')

            else:
                continue

        except ValueError:
            continue



def add(table):
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    while True:
        try:
            current_product = Product.get_product()
            current_product.set_quantity_sum()
            table.append(current_product.__dict__)
            print(table)

            print('Select another product or exit using Ctrl-D')

        except ValueError as e:
                    print(e)
                    continue

