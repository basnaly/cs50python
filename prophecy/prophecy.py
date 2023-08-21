import csv

from cs50 import SQL

db = SQL("sqlite:///database.db")

with open("students.csv") as file:
    reader = csv.DictReader(file)

    list_houses = []
    for row in reader:
        print(row)
        # Add data to the student table
        db.execute("INSERT INTO students VALUES(?, ?)", row["student_name"], row["id"])

        # Add data to the houses table
        if row["houses"] not in list_houses:
            list_houses.append(row["houses"])
            db.execute("INSERT INTO houses VALUES(?, ?)", row["house"], row["head"])

        # Add data to the assignments table
        db.execute("INSERT INTO assignments VALUES(?, ?)", row["id"], list_houses.index(row["house"]) + 1)