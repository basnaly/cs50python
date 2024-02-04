import sys
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
        with open('sys.argv[1]') as file:
            for line in file:
                row = line.rstrip().split('.')
                





main()
