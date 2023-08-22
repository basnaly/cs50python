SELECT people.name
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.year = 2004
   ORDER BY people.birth;



SELECT people.name, people.birth
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.year = 2004
   ORDER BY people.birth;