SELECT movies.title, people.name
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name = 'Bradley Cooper' AND people.name = 'Jennifer Lawrence';
