import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    name, extention = sys.argv[1].lstrip().split('.')
    if extention != 'csv':
        sys.exit('Not a CSV file')

    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                #  headers = line.rstrip().split(',')
                print(row)
                # name, large, small = line.rstrip().split(',')
                # print(tabulate(name, large, small, headers, tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')


main()
