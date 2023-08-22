
SELECT DISTINCT bradley_movies.title FROM

   (SELECT movies.id as id, movies.title as title
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name ='Bradley Cooper') AS bradley_movies,

   people JOIN stars
   ON people.id = stars.person_id
   AND stars.movie_id = bradley_movies.id
   WHERE people.name = 'Jennifer Lawrence';

+-------------------------+
|          title          |
+-------------------------+
| Silver Linings Playbook |
| Serena                  |
| American Hustle         |
| Joy                     |
+-------------------------+