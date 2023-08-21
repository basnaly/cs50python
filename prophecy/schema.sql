sqlite3 database.db

CREATE TABLE students (
    id INTEGER,
    student_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE houses (
    id INTEGER,
    house_name TEXT,
    head_name TEXT,
    PRIMARY KEY(id)
);

CREATE TABLE assignments (
    student_id INTEGER,
    house_id INTEGER,
    PRIMARY KEY students REFERENCES student_id (id),
)