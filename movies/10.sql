SELECT DISTINCT people.name
   FROM people, ratings JOIN directors
   ON people.id = directors.person_id AND directors.movie_id = ratings.movie_id
   WHERE ratings.rating >= 9.0;



SELECT DISTINCT people.name, ratings.rating
   FROM people, ratings JOIN directors
   ON people.id = directors.person_id AND directors.movie_id = ratings.movie_id
   WHERE ratings.rating >= 9.0;

| Michael Kirk                         | 10.0   |
| Kelly Rundle                         | 9.1    |
| Stephen Dassatti                     | 9.4    |
| Michalis Stavropoulos                | 9.4    |
| Ron Bourke                           | 9.0    |
| Aya Somech                           | 9.5    |
| Randon Bopp                          | 9.4    |
| Luigi Campi                          | 9.2    |
| Orlando Rojas                        | 9.7    |
| Joe Lujan                            | 9.6    |