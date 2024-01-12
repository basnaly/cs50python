SELECT DISTINCT people.name
    FROM people,

    (SELECT movies.id AS id
    FROM movies, people
    JOIN stars
    ON movies.id = stars.movie_id
    AND stars.person_id = people.id
    WHERE people.name = 'Kevin Bacon' AND people.birth = 1958) AS kevin_movies

    JOIN stars
    ON people.id = stars.person_id
    WHERE stars.movie_id = kevin_movies.id AND NOT people.name = 'Kevin Bacon';
