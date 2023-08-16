import csv

from cs50 import SQL

db = SQL("sqlite:///favorites.db")

rows = db.execute(UPDATE shows SET title = INITCAP(LOWER(title));