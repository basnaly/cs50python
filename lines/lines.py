import sys

def main():
    count = 0
    while True:
        if len(sys.argv) == 1:
            sys.exit('Too few command-line arguments')

        elif len(sys.argv) > 2:
            sys.exit('Too many command-line arguments')

        # name, extention = sys.argv[1].lstrip().split('.')
        #     if extention != 'py':
        #         sys.exit('Not a Python file')

        else:
            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        count += 1
                    print(count)
            except FileNotFoundError:
                sys.exit('File does not exist')



main()
