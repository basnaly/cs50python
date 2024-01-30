import json
import requests
import sys


def main():

    if len(sys.argv) != 2:
        print('Missing command-line argument ')
    try:
        elif float(sys.argv[1]):
            amount = float(sys.argv[1])
    except ValueError:
        print('Command-line argument is not a number ')

    

main()
