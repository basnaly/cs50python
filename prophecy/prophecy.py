import csv

db = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.append(row)
        db.execute("UPDATE students SET title = ? WHERE title LIKE ?", updated_title, row["title"])

    print(db)


