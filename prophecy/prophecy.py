import csv

from cs50 import SQL

db = SQL("sqlite:///database.db")

with open("students.csv") as file:
    reader = csv.DictReader(file)

    house_names = []
    for row in reader:
        db.execute("INSERT INTO students (student_name, id) VALUES (?, ?)", row["student_name"], row["id"])
        if row["house"] in house_names:
            continue
        else:
            house_names.append(row["house"])
            result = db.execute("INSERT INTO houses (house_name, head_name) VALUES (?, ?)", row["house"], row["head"])

        print(result)


