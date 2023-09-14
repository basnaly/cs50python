from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

import math
from datetime import datetime

from helpers import login_required, apology, lookup

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///articles.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "GET":
        return render_template("index.html", data = [])

    else:
        article_type = request.form.get("article_type")
        keyword = request.form.get("keyword")
        language = request.form.get("language")

        data = lookup(article_type, keyword, language)

        user_id = session["user_id"]

        if user_id:

            # Update search_history table
            user_search_history_table = f"search_history_{user_id}"
            db.execute(
                "INSERT INTO ? (article_type, keyword, language, date) VALUES(?, ?, ?, ?)",
                user_search_history_table,
                article_type,
                keyword,
                language,
                datetime.now(),
            )

        return render_template("index.html", keyword=keyword.title(), data=data or [], isLoggedIn = user_id )


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
            return apology("must provide username", 400)

        list_users = db.execute(
            "SELECT username FROM users WHERE username LIKE ?", username
        )

        if list_users:
            return apology("username is exist", 400)

        if not password:
            return apology("must provide password", 400)

        if len(password) < 3:
            return apology("password must have at least 3 symbols", 400)

        if password != confirmation:
            return apology("confirmation does't match to password", 400)

        if validate_password(password) == False:
            return apology("the password doesn't match", 400)

        # Insert the new user into users db
        hash_user_password = generate_password_hash(password)

        user_id = db.execute(
            "INSERT INTO users (username, hash) VALUES(?, ?)",
            username,
            hash_user_password,
        )

        # Remember which user has logged in
        session["user_id"] = user_id

        # Create articles table
        user_articles_table = f"articles_{user_id}"
        db.execute(
            "CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, keyword TEXT NOT NULL, source TEXT NOT NULL, author TEXT NOT NULL, title TEXT NOT NULL, url TEXT NOT NULL, published DATE);",
            user_articles_table,
        )

        # Create search history table
        user_search_history_table = f"search_history_{user_id}"
        db.execute(
            "CREATE TABLE ? (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, article_type TEXT NOT NULL, keyword TEXT NOT NULL, language TEXT NOT NULL, date DATE);",
            user_search_history_table,
        )

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", username
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], password
        ):
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


@app.route("/history" , methods=["GET", "POST"])
@login_required
def show_history():

    user_id = session["user_id"]

    if request.method == "GET":

        data = []

        user_search_history_table = f"search_history_{user_id}"
        list_search_history = db.execute("SELECT * FROM  ?;", user_search_history_table)

        for i, element in enumerate(list_search_history):
            id = element["id"]
            nn = i + 1
            article_type = element["article_type"]
            if article_type == "everything":
                article_type = "Articles"
            else:
                article_type = "Breaking news"

            keyword = element["keyword"]
            language = element["language"]
            date = element["date"]

            data.append(
                {
                    "id": id,
                    "nn": nn,
                    "article_type": article_type,
                    "keyword": keyword,
                    "language": language,
                    "date": date,
                }
            )

        return render_template("history.html", data=data)

    else:
        search_article_data = request.json["article"]
        search_article_id = search_article_data["id"]

        user_search_history_table = f"search_history_{user_id}"
        search_history_row = db.execute("SELECT * FROM  ? WHERE id = ?;", user_search_history_table, search_article_id)
        print(search_history_row)

        return {"path": "/"}

@app.route("/save-article", methods=["POST"])
@login_required
def save_article():

    user_id = session["user_id"]

    add_article = request.json["article"]

    keyword = add_article["keyword"]
    title = add_article["title"]
    source = add_article["source_name"]
    author = add_article["author"]
    url = add_article["url"]
    published = add_article["publishedAt"]
    print(keyword, title)

    user_articles_table = f"articles_{user_id}"
    db.execute(
        "INSERT INTO ? (keyword, title, source, author, url, published) VALUES (?, ?, ?, ?, ?, ?);",
        user_articles_table,
        keyword,
        title,
        source,
        author,
        url,
        published
    )

    return {"message": "The article was saved"}


@app.route("/articles", methods=["GET", "POST"])
@login_required
def saved_articles():

    user_id = session["user_id"]

    data = []

    user_saved_articles_table = f"articles_{user_id}"
    list_saved_articles = db.execute("SELECT * FROM  ?;", user_saved_articles_table)

    for i, element in enumerate(list_saved_articles):
        nn = i + 1
        keyword = element["keyword"]
        source = element["source"]
        author = element["author"]
        title = element["title"]
        url = element["url"]
        published = element["published"]

        data.append(
            {
                "nn": nn,
                "keyword": keyword,
                "source": source,
                "author": author,
                "title": title,
                "url": url,
                "published": published,
            }
        )

    return render_template("articles.html", data=data)