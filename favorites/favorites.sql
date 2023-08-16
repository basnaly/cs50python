sqlite3 favorites.db

.schema

SELECT * FROM shows;

UPDATE INITCAP (title) AS new_title FROM shows;

UPDATE INITCAP (title) FROM shows;

UPDATE shows SET title = LOWER(title);

UPDATE shows SET title = LOWER(title);
