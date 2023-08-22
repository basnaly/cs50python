SELECT movies.title, people.name
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name = 'Bradley Cooper' AND people.name = 'Jennifer Lawrence';

list the titles of all movies in which both Bradley Cooper and
Jennifer Lawrence starred