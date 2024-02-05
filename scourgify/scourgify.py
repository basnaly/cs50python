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
                fool_name = row[0:1]
                # first, last = row[0:1].split(',')
                print(fool_name)

    except FileNotFoundError:
        sys.exit('File does not exist')



main()
