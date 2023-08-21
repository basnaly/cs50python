sqlite3 songs.db

.schema

CREATE TABLE songs (
    id INTEGER,
    name TEXT,
    artist_id INTEGER,
    danceability REAL,
    energy REAL,
    key INTEGER,
    loudness REAL,
    speechiness REAL,
    valence REAL,
    tempo REAL,
    duration_ms INTEGER
);
CREATE TABLE artists (
    id INTEGER,
    name TEXT
);

SELECT * FROM songs;

+-----+---------------------------------------------------------+-----------+--------------+--------+-----+----------+-------------+---------+---------+-------------+
| id  |                          name                           | artist_id | danceability | energy | key | loudness | speechiness | valence |  tempo  | duration_ms |
+-----+---------------------------------------------------------+-----------+--------------+--------+-----+----------+-------------+---------+---------+-------------+
| 1   | God's Plan                                              | 23        | 0.754        | 0.449  | 7   | -9.211   | 0.109       | 0.357   | 77.169  | 198973      |
| 2   | SAD!                                                    | 67        | 0.74         | 0.613  | 8   | -4.88    | 0.145       | 0.473   | 75.023  | 166606      |
| 3   | rockstar (feat. 21 Savage)                              | 54        | 0.587        | 0.535  | 5   | -6.09    | 0.0898      | 0.14    | 159.847 | 218147      |
| 4   | Psycho (feat. Ty Dolla $ign)                            | 54        | 0.739        | 0.559  | 8   | -8.011   | 0.117       | 0.439   | 140.124 | 221440      |
| 5   | In My Feelings                                          | 23        | 0.835        | 0.626  | 1   | -5.833   | 0.125       | 0.35    | 91.03   | 217925      |
| 6   | Better Now                                              | 54        | 0.68         | 0.563  | 10  | -5.843   | 0.0454      | 0.374   | 145.028 | 231267      |
| 7   | I Like It                                               | 15        | 0.816        | 0.726  | 5   | -3.998   | 0.129       | 0.65    | 136.048 | 253390      |
 ...

 SELECT * FROM artists;

 +----+---------------------+
| id |        name         |
+----+---------------------+
| 1  | 5 Seconds of Summer |
| 2  | 6ix9ine             |
| 3  | Anitta              |
| 4  | Anne-Marie          |
| 5  | Ariana Grande       |
| 6  | Bazzi               |
| 7  | Bebe Rexha          |
 ...