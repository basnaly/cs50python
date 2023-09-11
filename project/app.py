import datetime

from flask import redirect, render_template, session

def lookup():
    """Look up quote for symbol."""

    # Prepare API request
    # symbol = symbol.upper()
    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=7)

    # Yahoo Finance API

    url = 'https://partners.api.skyscanner.net/apiservices/v3/flights/live/search/create'
    headers = {
        "User-Agent": "python-requests",
        "Accept": "*/*",
        "x-api-key": "sh428739766321522266746152871799",
    }
    data = {
        "query":{
            "market":"UK",
            "locale":"en-GB",
            "currency":"GBP",
            "query_legs":
            [
                {
                    "origin_place_id":{"iata":"LHR"},
                    "destination_place_id":{"iata":"SIN"},
                    "date":{"year":2022,"month":12,"day":22}
                }
            ],
            "adults":1,
            "cabin_class":"CABIN_CLASS_ECONOMY"}

    }


    # url = (
    #     f"https://query1.finance.yahoo.com/v7/finance/download/{urllib.parse.quote_plus(symbol)}"
    #     f"?period1={int(start.timestamp())}"
    #     f"&period2={int(end.timestamp())}"
    #     f"&interval=1d&events=history&includeAdjustedClose=true"
    # )

    # Query API
    try:
        response = requests.post(
            url,
            # cookies={"session": str(uuid.uuid4())},
            headers = headers,
            data = data
        )
        print(response)

        # # CSV header: Date,Open,High,Low,Close,Adj Close,Volume
        # quotes = list(csv.DictReader(response.content.decode("utf-8").splitlines()))
        # quotes.reverse()
        # price = round(float(quotes[0]["Adj Close"]), 2)
        # return {"name": symbol, "price": price, "symbol": symbol}

    except (requests.RequestException, ValueError, KeyError, IndexError):
        return None

lookup()