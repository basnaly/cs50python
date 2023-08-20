import csv

db = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

rows = db.execute("SELECT * FROM shows")

    for row in reader:
        db.append(row)

    print(db)


