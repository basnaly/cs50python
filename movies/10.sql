SELECT DISTINCT people.name, ratings.rating
   FROM people, ratings JOIN directors
   ON people.id = directors.person_id AND directors.movie_id = ratings.movie_id
   WHERE ratings.rating >= 9.0;

   list the names of all people who have directed a movie that
   received a rating of at least 9.0.