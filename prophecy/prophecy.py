import csv

db = []

with open("students.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        db.append(row)
        db.execute("INSERT INTO students (student_name, id) VALUES (?, ?)", row["student_name"], row["id"])

        db.execute("INSERT INTO houses (house_name, head_name) VALUES (?, ?)", row["house_name"], row["head_name"])

        
    print(db)


