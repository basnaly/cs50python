import requests
import sys
import json


def main():
    try:
        if len(sys.argv) != 2:
            sys.exit('Missing command-line argument')
        elif sys.argv[1].isdigit() == False:
            sys.exit('Command-line argument is not a number')

        
    except requests.RequestException:
        print('Error')


main()
