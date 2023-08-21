SELECT AVG(energy) FROM songs JOIN artists ON songs.artist_id = artists.id WHERE artists.name = "Drake";

+-------------+
| AVG(energy) |
+-------------+
| 0.599       |
+-------------+

SELECT AVG(energy), songs.name, artists.name FROM songs JOIN artists ON songs.artist_id = artists.id WHERE artists.name = "Drake";

+-------------+------------+-------+
| AVG(energy) |    name    | name  |
+-------------+------------+-------+
| 0.599       | God's Plan | Drake |
+-------------+------------+-------+

