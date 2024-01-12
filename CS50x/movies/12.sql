SELECT DISTINCT movies.title
   FROM people, movies,

   (SELECT movies.id AS id
   FROM movies, people
   JOIN stars
   ON movies.id = stars.movie_id
   AND people.id = stars.person_id
   WHERE people.name = 'Bradley Cooper') AS bradley_movie

   JOIN stars
   ON people.id = stars.person_id
   AND movies.id = stars.movie_id
   WHERE movies.id = bradley_movie.id AND people.name = 'Jennifer Lawrence';


-- +-------------------------+
-- |          title          |
-- +-------------------------+
-- | Silver Linings Playbook |
-- | Serena                  |
-- | American Hustle         |
-- | Joy                     |
-- +-------------------------+

