SELECT AVG(ratings.rating) FROM ratings JOIN movies ON movies.id = ratings.movie_id WHERE movies.year = 2012;


-- +---------------------+
-- | AVG(ratings.rating) |
-- +---------------------+
-- | 6.29787154592979    |
-- +---------------------+
