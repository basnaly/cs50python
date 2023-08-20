import csv

from cs50 import SQL



db = SQL("sqlite:///favorites.db")

rows = db.execute("UPDATE shows SET title = ? WHERE title = ?", updated_title, row["title"])

for row in rows:
    updated_title = row["title"].title()



