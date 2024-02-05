import sys
import csv


def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    buffer = []
    try:
        with open(sys.argv[1]) as file_read:
            with open(sys.argv[2], 'a') as file_write:
                reader = csv.DictReader(file_read)
                writer = csv.DictWriter(file_write, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    first, last = row['name'].split(',')
                    house = row['house']
                    writer.writerow({})


        # with open(sys.argv[1]) as file:
        #     reader = csv.DictReader(file)
        #     for row in reader:
        #         first, last = row['name'].split(',')
        #         house = row['house']
        #         buffer.append({'first': first, 'last': last, 'house': house})

        # with open(sys.argv[2], 'a') as file:
        #     writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        #     writer.writeheader()
        #     for row in buffer:
        #         writer.writerow(row)

    except FileNotFoundError:
        sys.exit('File does not exist')



main()
