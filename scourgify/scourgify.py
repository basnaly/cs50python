import sys, csv


def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments ')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    buffer = []
    try:
        with open(sys.argv[1]) as reader_file:
            reader = csv.DictReader(reader_file)
            for row in reader:
                first, last = row['name'].split(',')
                house = row['house']
                buffer.append({'first': first, 'last': last, 'house': house})

        with open(sys.argv[2], 'w') as writer_file:
            writer = csv.DictWriter(writer_file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in buffer:
                writer.writerow(row)

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]} file')



main()
