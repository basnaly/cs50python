import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    before = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                first, last = row['name'].split(',')
                house = row['house']
                before.append({'first': first, 'last': last, 'house': house})

        with open(sys.argv[2], 'a') as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerow(before)

    except FileNotFoundError:
        sys.exit('File does not exist')



main()
