import csv

from cs50 import SQL

db = SQL("sqlite:///favorites.db")

rows = db.execute("SELECT * FROM shows")

for row in rows:
    updated_title = row["title"].title()
    db.execute("UPDATE shows SET title = ? WHERE title LIKE ?", updated_title, row["title"])


