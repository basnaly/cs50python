SELECT DISTINCT people.name FROM

  (SELECT movies.id as id
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name = 'Kevin Bacon') AS Kevin_movies,

   stars JOIN people
   ON people.id = stars.person_id
   AND Kevin_movies.id = stars.movie_id
   WHERE NOT people.name = 'Kevin Bacon' ORDER BY people.name;


+------------------------+
|          name          |
+------------------------+
| Air Supply             |
| Alec Baldwin           |
| Alison Lohman          |
| Amanda Seyfried        |
| Andreas Michera        |
| Andy Garcia            |
| Andy Peake             |
| Anna Chlumsky          |
| Anthony LaPaglia       |
| Avery Tiiu Essex       |
| Barbara Barrie         |
| Ben Affleck            |
| Bill Gerber            |
| Bill Paxton            |
| Bob Balaban            |
| Bob Hoskins            |
 ...