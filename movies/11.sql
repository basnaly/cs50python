SELECT DISTINCT people.title, people.name
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name = 'Chadwick Boseman'
   ORDER BY people.birth;


list the titles of the five highest rated movies (in order) that
Chadwick Boseman starred in, starting with the highest rated.