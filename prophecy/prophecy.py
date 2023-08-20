import csv

db = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.append(row)
        db.execute("UPDATE students SET student_name = ? WHERE title = ?", row["student_name"], "")
        db.execute("UPDATE students SET id = ? WHERE id = ?", row["id"], "")

        db.execute("UPDATE houses SET house_name = ? WHERE house_name = ?", row["house_name"], "")
        db.execute("UPDATE houses SET head_name = ? WHERE head_name = ?", row["head_name"], "")

    print(db)


