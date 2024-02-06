import sys, csv


def main():

    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments ')
    elif len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')

    # 2-nd concept. Open sys.argv[1] file. Open sys.argv[2] file. Read data from sys.argv[1] file.
    # Write data to sys.argv[2] file and create headers into sys.argv[2] file
    # After that open sys.argv[2] file, create headers, write data from buffer to the file using loop.
    try:
        with open(sys.argv[1]) as reader_file:
            with open(sys.argv[2], 'a') as writer_file:
                reader = csv.DictReader(reader_file)
                writer = csv.DictWriter(writer_file, fieldnames=['first', 'last', 'house'])
                writer.writeheader()
                for row in reader:
                    first, last = row['name'].split(',')
                    house = row['house']
                    writer.writerow({'first': first, 'last': last, 'house': house})

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]} file')


main()


    # 1-st concept. Open, read data from sys.argv[1] file and add content to buffer.
    # After that open sys.argv[2] file, create headers, write data from buffer to the file using loop.
    # buffer = []
    # try:
    #     with open(sys.argv[1]) as reader_file:
    #         reader = csv.DictReader(reader_file)
    #         for row in reader:
    #             first, last = row['name'].split(',')
    #             house = row['house']
    #             buffer.append({'first': first, 'last': last, 'house': house})

    #     with open(sys.argv[2], 'w') as writer_file:
    #         writer = csv.DictWriter(writer_file, fieldnames=['first', 'last', 'house'])
    #         writer.writeheader()
    #         for row in buffer:
    #             writer.writerow(row)

    # except FileNotFoundError:
    #     sys.exit(f'Could not read {sys.argv[1]} file')
