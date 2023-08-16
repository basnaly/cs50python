import csv

from cs50 import SQL

db = SQL("sqlite:///favorites.db")

rows = db.execute("SELECT * FROM shows")

for row in rows:
    title = row.title()
    db.execute("UPDATE shows SET title = ?", title)