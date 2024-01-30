import json
import requests
import sys


def main():

    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument ')
    try:
        if float(sys.argv[1]):
            amount = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number ')

    response = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json'
    )

    data = response.json()
    usd_rate_float = data['bpi']['USD']['rate_float']
    print(usd_rate_float)

main()
