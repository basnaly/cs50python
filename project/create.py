import csv, sys
from tabulate import tabulate
# print install tabulate

from product import Product
from termcolor import cprint
from constants import CSV_FILE, FIELDNAMES, FARM_LIST


def create():
    cprint('\nHello! Welcome to our online organic farm store!', 'green')
    cprint('Pick you option: \n', 'green')

    # Display farm list
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["Name"]} {item["Icon"]} {item["Price/Kg"]}')

    try:
        list_products = []

        # Open csv file and clean it from previous data
        with open(CSV_FILE, mode='w', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

            while True:
                try:
                    # Create new product
                    current_product = Product.get_product()

                    exists_products = [product['Name'] for product in list_products]

                    # Check if the new product is already in the cart
                    if current_product.name in exists_products:
                        cprint(f'You already have {current_product.name} in your cart!', 'green')
                        cprint('If you want to edit this product, please run `python project.py -m edit`', 'green')
                        continue

                    # Set quantity of the new product and calculate the sum
                    current_product.set_quantity_sum()

                    # Save new product to csv file
                    current_product.save_to_csv(writer)

                    # Add new product into list products as dict
                    list_products.append(current_product.get_product_obj())

                    display_cart(list_products)

                    cprint('Select another product or exit using Ctrl-D', 'green')

                except ValueError as e:
                    continue

                # If user exit using Ctrl-D, print the following messages:
                except EOFError:
                    cprint('\nRun `python project.py -m edit` to edit the order.', 'green')
                    cprint('Run `python project.py -m finish` to complete the order.', 'green')
                    break

    except FileNotFoundError:
        sys.exit('File not found')


def display_cart(list_products):

    # Display list products that user added
    print(tabulate(list_products, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(list_products)]))

    # Add total sum after the table
    total = 0
    for product in list_products:
        total += round(float(product['Sum $']), 2)
    print(f'Total: ${round(total, 2)}')
