import csv

from cs50 import SQL

db = SQL("sqlite:///database.db")

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        # Add data to the student table
        db.execute("INSERT INTO students VALUES(?,?)", )