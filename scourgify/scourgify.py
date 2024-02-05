import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first, last = row['name'].split(',')
                print(first, last)

    except FileNotFoundError:
        sys.exit('File does not exist')



main()
