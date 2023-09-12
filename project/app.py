import datetime
import pytz
import requests

from flask import redirect, render_template, session

api_key = "c237f389d5674012bb0ca74e4f86675f"

def lookup(query):
    """Look up quote for symbol."""



    # Prepacre API request
    # symbol = symbol.upper()
    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=1)

    # Yahoo Finance API

    # GET https://newsapi.org/v2/everything?q=Apple&from=2023-09-12&sortBy=popularity&apiKey=API_KEY


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


    # try:
    #     response = requests.post(
    #         url,
    #         # cookies={"session": str(uuid.uuid4())},
    #         headers = headers,
    #         json = data
    #     )
    #     result_json = response.json()
    #     session_token = result_json["sessionToken"]
    #     print(session_token)
    #     print(result_json["content"]["results"])


    # except (requests.RequestException, ValueError, KeyError, IndexError) as e:
    #     return None

lookup("google")