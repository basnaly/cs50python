SELECT name, danceability, energy, valence FROM songs WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;

+---------------------------------------------+--------------+--------+---------+
|                    name                     | danceability | energy | valence |
+---------------------------------------------+--------------+--------+---------+
| Dura                                        | 0.791        | 0.848  | 0.828   |
| Me Niego                                    | 0.777        | 0.779  | 0.768   |
| Feel It Still                               | 0.801        | 0.795  | 0.754   |
| 1, 2, 3 (feat. Jason Derulo & De La Ghetto) | 0.792        | 0.895  | 0.794   |
| Criminal                                    | 0.814        | 0.813  | 0.839   |
+---------------------------------------------+--------------+--------+---------+