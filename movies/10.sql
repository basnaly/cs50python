SELECT DISTINCT people.name
   FROM people, ratings JOIN directors
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.year = 2004
   ORDER BY people.birth;

   list the names of all people who have directed a movie that
   received a rating of at least 9.0.