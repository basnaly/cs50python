sqlite3 favorites.db

.schema

SELECT * FROM shows;

SELECT * FROM shows WHERE title = "how i met your mother";

UPDATE shows SET title = "How I Met Your Mother" WHERE title LIKE "How I Met Your Mother";