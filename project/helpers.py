import datetime
import pytz
import requests

from flask import redirect, render_template, session

api_key = "c237f389d5674012bb0ca74e4f86675f"

def apology(message, code=400):
    """Render message as an apology to user."""

    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("apology.html", top=code, bottom=escape(message)), code


def lookup(keyword):
    """Look for keyword."""

    end = datetime.datetime.now(pytz.timezone("US/Eastern"))
    start = end - datetime.timedelta(days=1)

    # Query API
    try:

        url = ('https://newsapi.org/v2/everything?'
        f'q={keyword}&'
        f'from={start.strftime("%Y-%m-%d")}&'
        'sortBy=popularity&'
        f'apiKey={api_key}')

        response = requests.get(url)

        # print(response.json())

        articles = response.json()['articles']
        for element in articles:
            element["publishedAt"] = datetime.datetime.strptime(element["publishedAt"], "%Y-%m-%dT%H:%M:%SZ").strftime("%Y-%m-%d %H:%M")
        return articles

    except (requests.RequestException, ValueError, KeyError, IndexError) as e:
        print(e)
        return []