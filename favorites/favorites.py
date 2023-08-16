import csv

from cs50 import SQL

def main():
    db = SQL("sqlite:///favorites.db")

    rows = db.execute("SELECT * FROM shows")

    for row in rows:
        print(row)
        title = row["title"].title()
        db.execute("UPDATE shows SET title = ? WHERE title = ? ", (title, row["title"]))

main()