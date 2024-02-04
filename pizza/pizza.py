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
            i = 0
            for row in reader:
                if i == 0:
                    headers = row
                print(headers)
                print(row)
                name, large, small = line.rstrip().split(',')
                i += 1
                # print(tabulate(name, large, small, headers, tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')


main()
