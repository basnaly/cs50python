import datetime
import pytz
import requests

from flask import redirect, render_template, session

def lookup():
    """Look up quote for symbol."""

    # Prepare API request
    # symbol = symbol.upper()
    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=7)

    # Yahoo Finance API

    GET https://newsapi.org/v2/everything?q=Apple&from=2023-09-12&sortBy=popularity&apiKey=API_KEY


    # Query API
    url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2023-09-12&'
       'sortBy=popularity&'
       'apiKey=API_KEY')

    response = requests.get(url)

    print r.json


    try:
        response = requests.post(
            url,
            # cookies={"session": str(uuid.uuid4())},
            headers = headers,
            json = data
        )
        result_json = response.json()
        session_token = result_json["sessionToken"]
        print(session_token)
        print(result_json["content"]["results"])

        # # CSV header: Date,Open,High,Low,Close,Adj Close,Volume
        # quotes = list(csv.DictReader(response.content.decode("utf-8").splitlines()))
        # quotes.reverse()
        # price = round(float(quotes[0]["Adj Close"]), 2)
        # return {"name": symbol, "price": price, "symbol": symbol}

    except (requests.RequestException, ValueError, KeyError, IndexError) as e:
        return None

lookup()