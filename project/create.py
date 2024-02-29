import csv, sys
from tabulate import tabulate
from product import FARM_LIST, Product


def create():
    print('Hello! Welcome to our online organic farm store!')

    # Show farm list
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    try:
        list_products = []
        # Open csv file and clean it
        csv_file = 'basket.csv'
        with open(csv_file, mode='w', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price/Kg', 'Quantity', 'Sum $'])
            writer.writeheader()

            while True:
                try:
                    current_product = Product.get_product()
                    current_product.set_quantity_sum()
                    current_product.save_to_csv(writer)
                    list_products.append(current_product.__dict__)

                    print(list_products)
                    # get_data(list_products)

                    print('Select another product, finish your order or exit Ctrl-D')

                except ValueError as e:
                    print(e)
                    continue

                except EOFError:
                    print('\nYour order list:')
                    break

    except FileNotFoundError:
        sys.exit('File not found')


def get_data(list_products):
    csv_list = []
    # [{name:'gg'}]
    # try:
        # with open('basket.csv') as file:
    # reader = csv.DictReader(file)
    # for row in reader:
    #     csv_list.append(row)
    print(tabulate(list_products, headers='keys', tablefmt='grid'))

    total = 0
    for product in csv_list:
        total += float(product['Sum $'])
    return csv_list, total

    # except FileNotFoundError:
    #     sys.exit('File does not exist')
