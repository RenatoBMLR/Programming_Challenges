SELECT 
    movies.movie_title,
    movies.movie_year,
    f.director_name,
    f.actor_name,
    f.role
    FROM movies
        INNER JOIN 
            (
                SELECT 
                filtered_directors.director_name,
                filtered_actors.actor_name,
                filtered_actors.role,
                filtered_actors.movie_id
                FROM 
                    (
                    SELECT 
                        CONCAT(directors.director_first_name, directors.director_last_name) AS director_name,
                        movies_directors.movie_id
                        FROM directors
                            INNER JOIN movies_directors
                            ON movies_directors.director_id = directors.director_id
                    ) as filtered_directors
                    INNER JOIN
                    (SELECT 
                        CONCAT(actors.actor_first_name, actors.actor_last_name) AS actor_name,
                        movies_cast.movie_id,
                        movies_cast.role
                        FROM actors
                            INNER JOIN movies_cast
                            ON movies_cast.actor_id = actors.actor_id
                    ) as filtered_actors
                    ON filtered_actors.movie_id = filtered_directors.movie_id
                
            
            ) as f
        ON f.movie_id = movies.movie_id
        ORDER BY movies.movie_time ASC LIMIT 1
