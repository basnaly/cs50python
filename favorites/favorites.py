import csv

from cs50 import SQL

# Open database
db = SQL("sqlite:///favorites.db")

rows = db.execute("SELECT * FROM shows")
for row in rows:
    t