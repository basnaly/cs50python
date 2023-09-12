import datetime
import pytz
import requests

from flask import redirect, render_template, session

api_key = "c237f389d5674012bb0ca74e4f86675f"

def lookup(query):
    """Look up quote for symbol."""

    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=1)

    # Query API
    try:

        url = ('https://newsapi.org/v2/everything?'
        f'q={query}&'
        f'from={start.strftime("%Y-%m-%d")}&'
        'sortBy=popularity&'
        f'apiKey={api_key}')

        response = requests.get(url)

        # print(response.json())

        articles = response.json()['articles']
        print(articles[0])

    except (requests.RequestException, ValueError, KeyError, IndexError) as e:
        print(e)
        return None