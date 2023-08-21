sqlite3 favorites.db

.schema

SELECT * FROM shows;

+-----+------------------------------------+
| id  |               title                |
+-----+------------------------------------+
| 1   | How i met your mother              |
| 2   | The Sopranos                       |
 ...

UPDATE shows SET title = "How I Met Your Mother" WHERE title LIKE "How I Met Your Mother";

+-----+------------------------------------+
| id  |               title                |
+-----+------------------------------------+
| 1   | How I Met Your Mother              |
| 2   | The Sopranos                       |
 ...

 SELECT * FROM shows ORDER BY title;