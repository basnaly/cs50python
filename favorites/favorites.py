import csv

from cs50 import SQL

updated_title = row.title()

db = SQL("sqlite:///favorites.db")

for row in db:
    rows = db.execute("UPDATE shows SET title = ? WHERE title = ?", updated_title, row)