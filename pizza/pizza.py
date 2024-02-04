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

    table = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            i = 0
            for row in reader:
                print(row)
                if i == 0:
                    headers = row
                    name= headers[0]
                    print(headers)
                else:
                    table.append({'name': row[name], 'large': row['large'], 'small': row['small']})
                    i += 1
                print(table)
                # print(tabulate(name, large, small, headers, tablefmt='grid'))
    except FileNotFoundError:
        sys.exit('File does not exist')


main()
