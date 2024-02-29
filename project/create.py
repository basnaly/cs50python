import csv, sys

from product import FARM_LIST, Product


def create():
    print('Hello! Welcome to our online organic farm store!')

    # Show farm list
    print('Pick you option: ')
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["name"]} {item["icon"]} {item["price"]}')

    try:
        # Open csv file and clean it
        csv_file = 'basket.csv'
        with open(csv_file, mode='w', newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=['Name', 'Icon', 'Price $', 'Quantity', 'Sum $'])
            writer.writeheader()

            while True:
                try:
                    current_product = Product.get_product()
                    current_product.set_quantity_sum()
                    current_product.save_to_csv(writer)

                    print(current_product)

                    print('Select another product, finish your order or exit Ctrl-D')

                except ValueError as e:
                    print(e)
                    continue

                except EOFError:
                    print('\nYour order list:')
                    break

    except FileNotFoundError:
        sys.exit('File not found')

