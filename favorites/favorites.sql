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

 +-----+------------------------------------+
| id  |               title                |
+-----+------------------------------------+
| 116 | Adventure Time                     |
| 154 | Anne With An E                     |
| 31  | Archer                             |
| 100 | Arrested Development               |
| 24  | Arrow                              |
| 144 | Atlanta                            |
| 123 | Avatar                             |
| 34  | Avatar The Last Airbender          |
| 51  | Avatar The Last Airbender
 ...