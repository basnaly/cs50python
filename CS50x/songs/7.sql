SELECT AVG(energy) FROM songs JOIN artists ON songs.artist_id = artists.id WHERE artists.name = "Drake";

-- +-------------+
-- | AVG(energy) |
-- +-------------+
-- | 0.599       |
-- +-------------+

-- SELECT songs.name, artists.name, songs.energy FROM songs JOIN artists ON songs.artist_id = artists.id WHERE artists.name = "Drake";

-- +----------------+-------+--------+
-- |      name      | name  | energy |
-- +----------------+-------+--------+
-- | God's Plan     | Drake | 0.449  |
-- | In My Feelings | Drake | 0.626  |
-- | Nice For What  | Drake | 0.909  |
-- | Nonstop        | Drake | 0.412  |
-- +----------------+-------+--------+

-- (0.449 + 0.626 + 0.909 + 0.412) / 4 = 0.599