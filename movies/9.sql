SELECT DISTINCT people.name
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.year = 2004
   ORDER BY people.birth;



SELECT DISTINCT people.name, people.birth
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE movies.year = 2004
   ORDER BY people.birth LIMIT 20;

   +--------------------------+-------+
|           name           | birth |
+--------------------------+-------+
| Irela Bravo              | NULL  |
| Jean Badin               | NULL  |
| Amelia Barrett           | NULL  |
| Sean Miller              | NULL  |
| Jonny Spanish            | NULL  |
| Julienne Hanzelka Kim    | NULL  |
| G. Zachariah White       | NULL  |
| Sam Dean                 | NULL  |
| Sophia Dean              | NULL  |
| Will Dean                | NULL  |
| Kees Scholten            | NULL  |
| Juan Francisco Rodríguez | NULL  |
| David Burden             | NULL  |
| Kathryn Carner           | NULL  |
| Jerry Gelb               | NULL  |
| Kirsten Hill             | NULL  |
| Imma Villa               | NULL  |
| Rosario Sparno           | NULL  |
| Raffaele Di Florio       | NULL  |
| David Nicksic            | NULL  |
+--------------------------+-------+