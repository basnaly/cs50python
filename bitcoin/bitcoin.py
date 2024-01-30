import json
import requests
import sys


def main():
    # Check user's argument
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument ')
    try:
        # If user's argument is float save it to amount
        amount = float(sys.argv[1])
    except ValueError:
        sys.exit('Command-line argument is not a number ')

    # Send request
    response = requests.get(
        'https://api.coindesk.com/v1/bpi/currentprice.json'
    )
    # Get json from response
    data = response.json()
    usd_rate_float = data['bpi']['USD']['rate_float']
    result = usd_rate_float * amount
    print(f'${result:,.4f}')

main()
