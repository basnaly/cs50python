SELECT movies.title
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name IN ('Bradley Cooper', 'Jennifer Lawrence');


SELECT DISTINCT title FROM

   (SELECT title as title
   FROM people, movies JOIN stars
   ON people.id = stars.person_id AND movies.id = stars.movie_id
   WHERE people.name ='Bradley Cooper') AS bradley_movies, people

   JOIN stars
   ON people.id = stars.person_id
   AND title = bradley_movies.title
   WHERE people.name = 'Jennifer Lawrence';


-- +-------------------------------------------------------------+-------------------+
-- |                            title                            |       name        |
-- +-------------------------------------------------------------+-------------------+
-- | Bending All the Rules                                       | Bradley Cooper    |
-- | The A-Team                                                  | Bradley Cooper    |
-- | Case 39                                                     | Bradley Cooper    |
-- | The Midnight Meat Train                                     | Bradley Cooper    |
-- | New York, I Love You                                        | Bradley Cooper    |
-- | All About Steve                                             | Bradley Cooper    |
-- | Older Than America                                          | Bradley Cooper    |
-- | The Poker House                                             | Jennifer Lawrence |
-- | Causeway                                                    | Jennifer Lawrence |
-- | Silver Linings Playbook                                     | Bradley Cooper    |
-- | Silver Linings Playbook                                     | Jennifer Lawrence |
-- | Yes Man                                                     | Bradley Cooper    |
-- | The Hangover                                                | Bradley Cooper    |
-- | Don't Look Up                                               | Jennifer Lawrence |
-- | Limitless                                                   | Bradley Cooper    |
-- | Aloha                                                       | Bradley Cooper    |
-- | Serena                                                      | Bradley Cooper    |
-- | Serena                                                      | Jennifer Lawrence |
-- | X-Men: First Class                                          | Jennifer Lawrence |
-- | Passengers                                                  | Jennifer Lawrence |
-- | The Hunger Games                                            | Jennifer Lawrence |
-- | Winter's Bone                                               | Jennifer Lawrence |
-- | The Hangover Part II                                        | Bradley Cooper    |
-- | Lady Gaga: Encore                                           | Bradley Cooper    |
-- | A Star Is Born                                              | Bradley Cooper    |
-- | No Hard Feelings                                            | Jennifer Lawrence |
-- | House at the End of the Street                              | Jennifer Lawrence |
-- | Like Crazy                                                  | Jennifer Lawrence |
-- | American Hustle                                             | Bradley Cooper    |
-- | American Hustle                                             | Jennifer Lawrence |
-- | The Place Beyond the Pines                                  | Bradley Cooper    |
-- | The Words                                                   | Bradley Cooper    |
-- | The Hangover Part III                                       | Bradley Cooper    |
-- | The Hunger Games: Catching Fire                             | Jennifer Lawrence |
-- | The Hunger Games: Mockingjay - Part 1                       | Jennifer Lawrence |
-- | The Hunger Games: Mockingjay - Part 2                       | Jennifer Lawrence |
-- | Hollywood's Hard Hitters: Women in Action                   | Jennifer Lawrence |
-- | Guardians of the Galaxy                                     | Bradley Cooper    |
-- | Hit and Run                                                 | Bradley Cooper    |
-- | American Sniper                                             | Bradley Cooper    |
-- | Joy                                                         | Jennifer Lawrence |
-- | Joy                                                         | Bradley Cooper    |
-- | Burnt                                                       | Bradley Cooper    |
-- | A Beautiful Planet                                          | Jennifer Lawrence |
-- | Red Sparrow                                                 | Jennifer Lawrence |
-- | X-Men: Apocalypse                                           | Jennifer Lawrence |
-- | Surviving the Game - Making the Hunger Games: Catching Fire | Jennifer Lawrence |
-- | Hurricane of Fun: The Making of Wet Hot                     | Bradley Cooper    |
-- | Mother!                                                     | Jennifer Lawrence |
-- | X-Men: Dark Phoenix                                         | Jennifer Lawrence |
-- | Nightmare Alley                                             | Bradley Cooper    |
-- +-------------------------------------------------------------+-------------------+
