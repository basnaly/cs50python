import sys

def main():
    count = 0
    while True:
        if len(sys.argv) == 1:
            sys.exit('Too few command-line arguments')

        elif len(sys.argv) > 2:
            sys.exit('Too many command-line arguments')

        # Check if file is python
        name, extention = sys.argv[1].lstrip().split('.')
        if extention != 'py':
            sys.exit('Not a Python file')

        try:
            # Open file with name in sys.argv[1]
            with open(sys.argv[1]) as file:
                for line in file:
                    # If line not an empty string and not comment
                    if line.lstrip() != '' and not line.lstrip().startswith('#'):
                        count += 1
                print(count)
                break
        except FileNotFoundError:
            sys.exit('File does not exist')


main()
