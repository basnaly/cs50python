SELECT DISTINCT people.title, people.name, ratings.rating
   FROM people, movies JOIN ratings
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name = 'Chadwick Boseman'
   ORDER BY people.rating;


list the titles of the five highest rated movies (in order) that
Chadwick Boseman starred in, starting with the highest rated.