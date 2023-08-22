SELECT people.name
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.title = 'Toy Story';


-- SELECT people.name, movies.title
--    FROM people, movies JOIN stars
--    ON people.id = stars.person_id AND movies.id = stars.movie_id
--    WHERE movies.title = 'Toy Story';

-- +-------------+-----------+
-- |    name     |   title   |
-- +-------------+-----------+
-- | Tom Hanks   | Toy Story |
-- | Tim Allen   | Toy Story |
-- | Don Rickles | Toy Story |
-- | Jim Varney  | Toy Story |
-- +-------------+-----------+