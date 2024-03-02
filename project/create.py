import csv, sys
from tabulate import tabulate
from product import FARM_LIST, Product
from colorama import Fore, Back, Style
from termcolor import colored, cprint


def create():
    print('Hello! Welcome to our online organic farm store!')

    # Show farm list
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    try:
        list_products = []
        # Open csv file and clean it
        csv_file = 'cart.csv'
        with open(csv_file, mode='w', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price/Kg', 'Quantity', 'Sum $'])
            writer.writeheader()

            while True:
                try:
                    current_product = Product.get_product()
                    current_product.set_quantity_sum()
                    current_product.save_to_csv(writer)
                    list_products.append(current_product.__dict__)

                    # print(list_products)
                    display_cart(list_products)

                    print('Select another product or exit using Ctrl-D')

                except ValueError as e:
                    print(e)
                    continue

                except EOFError:
                    cprint('\nRun `python project.py -m edit` to edit the order.', 'green')
                    cprint('Run `python project.py -m finish` to complete the order.', 'green')
                    break

    except FileNotFoundError:
        sys.exit('File not found')


def display_cart(list_products):

    print(tabulate(list_products, headers='keys', tablefmt='grid'))

    total = 0
    for product in list_products:
        total += float(product['sum'])
    print(f'Total: ${total}')
