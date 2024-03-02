import csv, sys
from tabulate import tabulate
from termcolor import colored, cprint
import argparse
from product import FARM_LIST, Product


def edit():
    cprint('Here is your order:', 'blue')
    table = []
    try:
        csv_file = 'basket.csv'
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers='keys', tablefmt='grid'))
            cprint('What would you like to edit?', 'blue')
            cprint('To add new one type 1.', 'blue')
            cprint('To delete type 2, space and the name.', 'blue')
            cprint('To change quantity type 3, space, the name, space and the quantity you want to change to.', 'blue')

    except FileNotFoundError:
        sys.exit('File does not exist')





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

