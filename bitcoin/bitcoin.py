import requests
import sys
import json


def main():
    try:
        if len(sys.argv) != 2:
            sys.exit('Missing command-line argument')
        elif sys.argv[1].isdigit() == False:
            sys.exit('Command-line argument is not a number')

        response = requests.get(
            'https://api.coindesk.com/v1/bpi/currentprice.json'
        )
        data = response.json
        currencies = data['bpi']
        usd_rate = currencies['USD']['rate_float']
        print(usd_rate)

    except requests.RequestException:
        print('Error')


main()
