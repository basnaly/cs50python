import csv

from cs50 import SQL

db = SQL("sqlite:///database.db")

with open("students.csv") as file:
    reader = csv.DictReader(file)

    list_houses = []
    for row in reader:
        # Add data to the student table
        db.execute("INSERT INTO students (student_name, id) VALUES(?, ?)", row["student_name"], int(row["id"]))

        # Add data to the houses table
        if row["house"] not in list_houses:
            list_houses.append(row["house"])
            db.execute("INSERT INTO houses (house_name, head_name) VALUES(?, ?)", row["house"], row["head"])

        # Add data to the assignments table
        db.execute("INSERT INTO assignments (student_id, house_id) VALUES(?, ?)", int(row["id"]), list_houses.index(row["house"]) + 1)