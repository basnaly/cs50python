import csv

from cs50 import SQL

db = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.append(row)

    print(db)


