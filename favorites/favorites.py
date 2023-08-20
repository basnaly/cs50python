import csv

from cs50 import SQL

updated_title = row["title"].title()

db = SQL("sqlite:///favorites.db")

for row in rows:
    rows = db.execute("UPDATE shows SET title = ? WHERE title = ?", updated_title, row["title"])


