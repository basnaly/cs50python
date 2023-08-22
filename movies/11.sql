SELECT movies.title
   FROM people, movies, ratings JOIN stars
   ON people.id = stars.person_id
   AND movies.id = stars.movie_id
   AND movies.id = ratings.movie_id
   WHERE people.name = 'Chadwick Boseman'
   ORDER BY ratings.rating DESC
   LIMIT 5;




-- SELECT movies.title, people.name, ratings.rating
--    FROM people, movies, ratings JOIN stars
--    ON people.id = stars.person_id
--    AND movies.id = stars.movie_id
--    AND movies.id = ratings.movie_id
--    WHERE people.name = 'Chadwick Boseman'
--    ORDER BY ratings.rating DESC
--    LIMIT 5;


-- +--------------------------+------------------+--------+
-- |          title           |       name       | rating |
-- +--------------------------+------------------+--------+
-- | 42                       | Chadwick Boseman | 7.5    |
-- | Black Panther            | Chadwick Boseman | 7.3    |
-- | Marshall                 | Chadwick Boseman | 7.3    |
-- | Ma Rainey's Black Bottom | Chadwick Boseman | 6.9    |
-- | Get on Up                | Chadwick Boseman | 6.9    |
-- +--------------------------+------------------+--------+
