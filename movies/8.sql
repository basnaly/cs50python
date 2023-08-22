SELECT people.name, movies.title
   FROM people JOIN stars ON people.id = stars.person_id
   FROM movies JOIN start ON movies.id = stars.movie_id
   WHERE movies.title = 'Toy Story';


SELECT people.name, movies.title
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.title = 'Toy Story';