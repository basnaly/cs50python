SELECT people.name, movies.title
   FROM people JOIN stars ON people.id = stars.person_id
   FROM movies JOIN start ON movies.id = stars.movie_id
   WHERE movies.title = 'Toy Story';