import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

import math
from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    user_id = session["user_id"]

    data = []
    sum = 0

    portfolio_table = f"portfolio_{user_id}"
    list_shares = db.execute("SELECT * FROM ?", portfolio_table)

    for i, element in enumerate (list_shares):
        nn = i + 1
        symbol = element["symbol"]
        shares = int(element["shares"])
        price = lookup(symbol)
        total = (shares) * price["price"]
        sum += total
        data.append({"nn": nn, "symbol": symbol.upper(), "shares": shares, "price": price["price"], "total": total})

    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    cash = cash[0]["cash"]

    total_value = cash + sum

    return render_template("index.html", data = data, sum = sum, cash = cash, total_value = total_value)

@app.route("/add_cash", methods = ["GET", "POST"])
@login_required
def add_cash():

    # When requested via GET, display form to buy a cash.
    if request.method == "GET":
        return render_template("add_cash.html")

    # When form is submitted via POST, add cah to current cash.

    add_cash = request.form.get("add_cash")
    print(add_cash)

    if not add_cash:
        return apology("must provide sum of cash", 403)

    # Add cash to user table

    user_id = session["user_id"]

    current_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    print(current_cash)
    if not current_cash:
        return apology("user doesn't exist", 403)

    updated_cash = current_cash[0]["cash"] + float(add_cash)
    db.execute("UPDATE users SET cash = ? WHERE id = ?", updated_cash, user_id)

    transactions_table = f"transactions_{user_id}"
    db.execute("INSERT INTO ? (symbol, shares, price, date) VALUES(?, ?, ?, ?)", transactions_table, symbol, shares, price, datetime.now())

    return redirect("/")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # When requested via GET, display form to buy a stock.
    if request.method == "GET":
        return render_template("buy.html")

     # When form is submitted via POST, purchase the stock so long
     # as user can afford it.

    symbol = request.form.get("symbol")
    shares = request.form.get("shares")

    if not symbol:
        return apology("must provide symbol", 403)

    data = lookup(symbol)
    price = data["price"]
    if data == None:
        return apology("symbol doesnt exists", 403)

    if not shares:
        return apology("must provide number of shares", 403)

    shares = int(shares)

    if shares < 0:
        return apology("must provide positive number", 403)

    user_id = session["user_id"]

    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    if not user_cash:
        return apology("user doesn't exist", 403)

    current_user_cash = user_cash[0]["cash"]
    max_stocks_to_buy = math.floor( current_user_cash / price)

    if max_stocks_to_buy < shares:
        return apology(f"you can buy only {max_stocks_to_buy} stocks", 403)

    # Adding new SQL table
    # Decide on table name(s) and fields

    transactions_table = f"transactions_{user_id}"
    db.execute("INSERT INTO ? (symbol, shares, price, date) VALUES(?, ?, ?, ?)", transactions_table, symbol, shares, price, datetime.now())

    portfolio_table = f"portfolio_{user_id}"
    row_symbol = db.execute("SELECT * FROM ? WHERE symbol = ?", portfolio_table, symbol)

    if not row_symbol:
        db.execute("INSERT INTO ? (symbol, shares) VALUES(?, ?)", portfolio_table, symbol, shares)
    else:
        current_user_shares = int(row_symbol[0]["shares"])
        db.execute("UPDATE ? SET shares = ? WHERE symbol = ?", portfolio_table, current_user_shares + shares, symbol)

    updated_cash = db.execute("UPDATE users SET cash = ? WHERE id = ?", current_user_cash - (shares * price), user_id)

    return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    user_id = session["user_id"]
    history = []

    transactions_table = f"transactions_{user_id}"
    history_list = db.execute("SELECT * FROM ? ORDER BY date DESC", transactions_table)
    print(history_list)

    for i, element in enumerate (history_list):
        nn = i + 1
        symbol = element["symbol"]
        shares = element["shares"]
        price = float(element["price"])
        date = element["date"]
        class_name = "buy" if int(element["shares"]) > 0 else "sell"
        history.append({"nn": nn, "symbol": symbol.upper(), "shares": shares, "price": price, "date": date, "class_name" : class_name})

    return render_template("history.html", history = history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # When requested via GET, display form to request a stock quote.
    if request.method == "GET":
        return render_template("quote.html")

    # When form is submitted via POST, lookup the stock symbol by calling
    # the lookup function and display the results.
    else:
        symbol = request.form.get("symbol")

        # Ensure username was submitted
        if not symbol:
            return apology("must provide symbol", 403)

        data = lookup(symbol)
        print(data)

        if data == None:
            return apology("the symbol doesn't exist")

        return render_template("quoted.html", data = data)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    def validate_password(password):
        if len(password) < 3:
            return False

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Check for possible errors
        if not username:
            return apology("must provide username", 403)

        list_users = db.execute("SELECT username FROM users WHERE username LIKE ?", username)

        if list_users:
            return apology("username is exist", 403)

        elif not password:
            return apology("must provide password", 403)

        elif len(password) < 3:
            return apology("password must have at least 3 symbols", 403)

        elif password != confirmation:
            return apology("confirmation does't match to password", 403)

        elif validate_password(password) == False:
            return apology("the password doesn't match", 403)

        # Insert the new user into users db
        hash_user_password = generate_password_hash(password)

        user_id = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash_user_password)

        # Remember which user has logged in
        session["user_id"] = user_id

        # Create transactions table
        user_transaction_table = f"transactions_{user_id}"
        db.execute("CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, symbol TEXT NOT NULL, shares TEXT NOT NULL, price TEXT NOT NULL, date DATE);", user_transaction_table)

        # Create portfolio table
        user_portfolio_table = f"portfolio_{user_id}"
        db.execute("CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, symbol TEXT NOT NULL, shares TEXT NOT NULL);", user_portfolio_table)

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session["user_id"]

    portfolio_table = f"portfolio_{user_id}"
    transactions_table = f"transactions_{user_id}"

    # When requested via GET, display form to sell a stock.
    if request.method == "GET":

        # List of symbols in portfolio
        list_stocks = db.execute("SELECT symbol, shares FROM ?", portfolio_table)

        return render_template("sell.html", list_stocks = list_stocks)

    # When form is submitted via POST, check for errors and sell the
    # number of shares of stock and update user's cash

    symbol = request.form.get("symbol")
    shares = request.form.get("shares")

    if not symbol:
        return apology("must provide symbol", 403)

    # If symbol is not in portfolio

    list_symbols = db.execute("SELECT * FROM ? WHERE symbol LIKE ?", portfolio_table, symbol)

    if not list_symbols:
        return apology("must provide valid symbol", 403)

    data = lookup(symbol)
    price = data["price"]
    shares = int(shares)

    if data == None:
        return apology("symbol doesnt exists", 403)

    if not shares:
        return apology("must provide number of shares", 403)

    if shares < 0:
        return apology("must provide positive number", 403)

    list_shares = db.execute("SELECT shares FROM ? WHERE symbol LIKE ?", portfolio_table, symbol)
    user_shares = int(list_shares[0]["shares"])
    if shares > user_shares:

        return apology(f"you have only {user_shares} shares", 403)

    user_cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    if not user_cash:
        return apology("user doesn't exist", 403)

    current_user_cash = user_cash[0]["cash"]
    sold_stocks = shares * price
    sold_shares = shares * -1

    # Update shares of symbol in transactions_{user_id}
    db.execute("INSERT INTO ? (symbol, shares, price, date) VALUES(?, ?, ?, ?)", transactions_table, symbol, sold_shares, price, datetime.now())

    # Update shares of symbol in portfolio_{user_id}
    db.execute("UPDATE ? SET shares = ? WHERE symbol LIKE ?", portfolio_table, user_shares - shares, symbol)

    # If sold shares = current shares remove row
    if shares == user_shares:
        db.execute("DELETE FROM ? WHERE symbol LIKE ?", portfolio_table, symbol)

    # Update cash:
    db.execute("UPDATE users SET cash = ? WHERE id = ?", current_user_cash + sold_stocks, user_id)

    return redirect("/")

# sqlite3 finance.db
# .schema
# CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                     username TEXT NOT NULL,
#                     hash TEXT NOT NULL,
#                     cash NUMERIC NOT NULL DEFAULT 10000.00);

# CREATE TABLE sqlite_sequence(name,seq);
# CREATE UNIQUE INDEX username ON users (username);

# CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                 symbol TEXT NOT NULL,
#                 shares TEXT NOT NULL,
#                 date DATE);", f"transactions_{user_id}");

# CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
#                 symbol TEXT NOT NULL,
#                 shares TEXT NOT NULL);", f"portfolio_{user_id});

# +----+----------+--------------------------------------------------------------------------------------------------------+-------+
# | id | username |                                                  hash                                                  | cash  |
# +----+----------+--------------------------------------------------------------------------------------------------------+-------+
# | 1  | nat      | pbkdf2:sha256:600000$cFxRK2TL3GPv3dvi$28ac2675e8a7eb841385bf67edbc120b4cdcff3f403b3666dd15ffe116271784 | 10000 | 123 id=7
# | 2  | nataly   | pbkdf2:sha256:600000$mwZIOtpezAwi6KvY$f38f60712514819f522de47b0989a5580d924d21e3311f3ca792372cd98321e8 | 10000 | 345
# | 3  | alona    | pbkdf2:sha256:600000$QdRa93Z0UZsgHitF$14bd5e5a60c0029fd1429c5848ef3e84dbaaa0a5a71b4388436aec4a9f8624e1 | 10000 | 987
# | 4  | max      | pbkdf2:sha256:600000$AwlxJDvhMY50xyj2$0b534c7ca112a3db00fac0b123569fdba3a0d49eacad2e4151105ff224b077d6 | 10000 | max
# | 5  | alex     | pbkdf2:sha256:600000$zfXX1ARPI07E4WvT$9241e6a96d8ac163addfb533162371bd128dd0b3fd8cf47ee5746db430a563a3 | 10000 | lex
# | 6  | qwe      | pbkdf2:sha256:600000$qKteNzpGXVNRebDx$cb23241ec82fad81d4db1f11c2d16ef327b2049c1fe437894e117b5e6ee39a55 | 10000 | qwe
# +----+----------+--------------------------------------------------------------------------------------------------------+-------+

# SELECT * FROM transactions_7;
# +----+--------+--------+---------------------+
# | id | symbol | shares |        date         |
# +----+--------+--------+---------------------+
# | 1  | aapl   | 10     | 2023-09-08 14:48:26 |
# | 2  | tip    | 15     | 2023-09-08 14:48:46 |
# +----+--------+--------+---------------------+
# sqlite> SELECT * FROM portfolio_7;
# +----+--------+--------+
# | id | symbol | shares |
# +----+--------+--------+
# | 1  | aapl   | 10     |
# | 2  | tip    | 15     |
# +----+--------+--------+