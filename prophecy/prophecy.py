import csv

from cs50 import SQL

db = SQL("sqlite:///database.db")

with open("students.csv") as file:
    reader = csv.DictReader(file)

    house_names = []
    for row in reader:
        # Add data to students table
        db.execute("INSERT INTO students (student_name, id) VALUES (?, ?)", row["student_name"], row["id"])

        # Add data to houses table
        if row["house"] not in house_names:
            house_names.append(row["house"])
            result = db.execute("INSERT INTO houses (house_name, head_name) VALUES (?, ?)", row["house"], row["head"])

        print(result)

        # Add data to assignment table
        db.execute("INSERT INTO assignments (student_id, house_id) VALUES (?, ?)", row["id"], house_names.index(row["house"]) + 1)

