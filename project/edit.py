import csv, sys
from tabulate import tabulate
from termcolor import colored, cprint


def edit():
    cprint('Here is your order:', 'blue')
    try:
        table = []
        csv_file = 'basket.csv'
        with open(csv_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                table.append(row)
            print(tabulate(table, headers='keys', tablefmt='grid'))

    except FileNotFoundError:
        sys.exit('File does not exist')
