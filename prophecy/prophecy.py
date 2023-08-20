import csv

db = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.append(reader)

    print(db)