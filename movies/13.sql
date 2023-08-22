SELECT people.name, movies.title
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name = 'Kevin Bacon'
   WHERE ()






 list the names of all people who starred in a movie in
 which Kevin Bacon also starred