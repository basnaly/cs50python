import csv, sys
from tabulate import tabulate
# print install tabulate
from product import FARM_LIST, Product
from termcolor import cprint


def create():
    cprint('\nHello! Welcome to our online organic farm store!', 'green')

    # Show farm list
    cprint('Pick you option: \n', 'green')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["Name"]} {item["Icon"]} {item["Price/Kg"]}')

    try:
        list_products = []
        # Open csv file and clean it
        csv_file = 'cart.csv'
        with open(csv_file, mode='w', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price/Kg', 'Quantity', 'Sum $'])
            writer.writeheader()

            while True:
                try:
                    # Create current product
                    current_product = Product.get_product()

                    # Check if the current product is already in the cart
                    exists_products = [product['name'] for product in list_products]
                    if current_product.name in exists_products:
                        cprint(f'You already have {current_product.name} in your cart!', 'green')
                        cprint('If you want to edit this product, please run `python project.py -m edit`', 'green')
                        continue

                    # Set quantity to the current product and calculate sum
                    current_product.set_quantity_sum()

                    # Save current product to csv file
                    current_product.save_to_csv(writer)

                    # Add current product into list products in dict format
                    list_products.append(current_product.__dict__)

                    display_cart(list_products)

                    cprint('Select another product or exit using Ctrl-D', 'green')

                except ValueError as e:
                    continue

                # If user exit using Ctrl-D print next messages:
                except EOFError:
                    cprint('\nRun `python project.py -m edit` to edit the order.', 'green')
                    cprint('Run `python project.py -m finish` to complete the order.', 'green')
                    break

    except FileNotFoundError:
        sys.exit('File not found')


def display_cart(list_products):

    print(tabulate(list_products, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(list_products)]))

    total = 0
    for product in list_products:
        total += round(float(product['sum']), 2)
    print(f'Total: ${round(total, 2)}')
