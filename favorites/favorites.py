import csv

from cs50 import SQL

updated_title = row.title()

db = SQL("sqlite:///favorites.db")

rows = db.execute()