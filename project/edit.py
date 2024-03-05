import csv, sys
from tabulate import tabulate
from termcolor import cprint
from product import Product
from constants import CSV_FILE, FIELDNAMES, FARM_LIST, MAX_QUANTITY


def edit():
    cprint('Here is your order:', 'blue')
    table = []

    try:
        # Read data from csv file
        with open(CSV_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            # Add the data to table list
            for row in reader:
                table.append(row)

            # Calculate total sum of the cart
            total = 0
            for item in table:
                total += round(float(item['Sum $']), 2)

            # Display user's cart
            print(tabulate(table, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(table)]))
            cprint(f'Total: ${total}\n', attrs=['bold'])

    except FileNotFoundError:
        sys.exit('File does not exist')

    while True:
        try:
            # Inform user about options to continue
            cprint('What would you like to edit?', 'blue', attrs=['bold'])
            cprint('Your options are:', 'blue')
            cprint('1. To add new one type: "1".', 'blue')
            cprint('2. To delete type: "2 <x>", where x is the number of the product in the cart.', 'blue')
            cprint('3. To change quantity type: "3 <x> <y>" where x is the number of the product and y is a new amount.', 'blue')
            cprint('4. To exit and save use Ctrl-D.', 'blue')

            choice = input('Your choice: ').split(' ')

            # If user selected '1' call add function to add a new product to the cart
            if choice[0] == '1':
                add(table)

            # If user selected '2' call delete function to delete an existing product from the cart
            elif choice[0] == '2':
                delete(table, int(choice[1]) - 1)

            # If user selected '3' call change_quantity function
            elif choice[0] == '3':
                change_quantity(table, int(choice[1]) - 1, float(choice[2]))

            else:
                continue

            # Calculate total sum of all the products in the cart
            total = 0
            for item in table:
                total += round(float(item['Sum $']), 2)

            # Display updated list of user's products
            print(tabulate(table, headers='keys', tablefmt='grid', showindex=[i+1 for i,e in enumerate(table)]))
            cprint(f'Total: ${total}\n', attrs=['bold'])

        except ValueError as e:
            continue

        except EOFError:
            # When user exit using Ctrl-D, call save_to_cart function to save updated list of user's products to csv file
            save_to_cart(table)
            cprint('\nRun `python project.py -m edit` to edit the order.', 'blue')
            cprint('Run `python project.py -m finish` to complete the order.', 'blue')
            break


def add(table):
    print('Pick you option: ')

    # Display farm list
    for index, item in enumerate(FARM_LIST):
        print(f'{index+1}) {item["Name"]} {item["Icon"]} {item["Price/Kg"]}')

    try:
        # Create new product
        current_product = Product.get_product()

        exists_products = [product['Name'] for product in table]

        # Check if the current product is already in the cart
        if current_product.name in exists_products:
            cprint(f'You already have {current_product.name} in your cart!', 'blue')
            cprint('To change quantity type: "3 <x> <y>" where x is the number of the product and y is a new amount.', 'blue')
            return

        # Set quantity of the current product and calculate the sum
        current_product.set_quantity_sum()

        # Add the current product into the table
        table.append(current_product.get_product_obj())

    except ValueError as e:
        print(e)


def delete(table, index):

    # Delete product from table by its index
    table.pop(index)


def change_quantity(table, index, new_quantity):

    if index < 0 or index >= len(table):
        print('Index doesn\'t exist in the table')
        raise ValueError('Index doesn\'t exist in the table')

    if new_quantity < 0 and new_quantity > MAX_QUANTITY:
        print('New quantity mast be between 0 and 5')
        raise ValueError('New quantity mast be between 0 and 5')


    # Set new quantity
    table[index]['Quantity'] = new_quantity

    # Calculate sum of the product
    table[index]['Sum $'] = round(float(table[index]['Quantity']) * float(table[index]['Price/Kg']), 2)


def save_to_cart(table):

    # Save data from table into csv file
    with open(CSV_FILE, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        for row in table:
            writer.writerow(row)
