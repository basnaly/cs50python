SELECT movies.title, people.name, ratings.rating
   FROM people, movies, ratings JOIN stars
   ON people.id = stars.person_id
   AND movies.id = stars.movie_id
   AND movies.id = ratings.movie_id
   WHERE people.name = 'Chadwick Boseman'
   ORDER BY ratings.rating DESC
   LIMIT 5;


list the titles of the five highest rated movies (in order) that
Chadwick Boseman starred in, starting with the highest rated.