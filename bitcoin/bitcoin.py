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
        data = response.json()
        usd_rate = data['bpi']['USD']['rate_float']
        result = float(usd_rate) * float(sys.argv[1])
        print(f'${result:,.4f}')

    except requests.RequestException:
        print('Error')


main()
