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

    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]} file')



main()
