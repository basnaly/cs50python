

SELECT songs.name, artists.name FROM songs JOIN artists ON songs.artist_id = artists.id WHERE artists.name = "Post Malone";

+------------------------------+-------------+
|             name             |    name     |
+------------------------------+-------------+
| Better Now                   | Post Malone |
| Candy Paint                  | Post Malone |
| Congratulations              | Post Malone |
| I Fall Apart                 | Post Malone |
| Psycho (feat. Ty Dolla $ign) | Post Malone |
| rockstar (feat. 21 Savage)   | Post Malone |
+------------------------------+-------------+

-- SELECT table1.column_name1, table1.column_name2, table2.column_name3
-- FROM table1
-- INNER JOIN table2 ON table1.common_column = table2.common_column;