SELECT movies.title, ratings.rating
   ...> FROM movies JOIN ratings
   ...> ON movies.id = ratings.movie_id
   ...> WHERE movies.year = 2010
   ...> ORDER BY ratings.rating DESC,movies.title;



SELECT movies.title, ratings.rating
   ...> FROM movies JOIN ratings
   ...> ON movies.id = ratings.movie_id
   ...> WHERE movies.year = 2010
   ...> ORDER BY ratings.rating DESC,movies.title
   ...> LIMIT 10;
+--------------------------------------------------------+--------+
|                         title                          | rating |
+--------------------------------------------------------+--------+
| Amaren ideia                                           | 9.8    |
| The American Buffalo                                   | 9.8    |
| The Great Mystery                                      | 9.8    |
| Carolina, RI: The Smallest of the Small                | 9.6    |
| Moy otets Evgeniy                                      | 9.6    |
| Star War the Third Gathers: The Backstroke of the West | 9.6    |
| Born to Be Our Children: Romanian Adoption Stories     | 9.5    |
| I Breathe                                              | 9.5    |
| If I Should Fall                                       | 9.5    |
| JoJo Baby                                              | 9.5    |
+--------------------------------------------------------+--------+