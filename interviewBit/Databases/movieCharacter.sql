SELECT 
    CONCAT(directors.director_first_name, directors.director_last_name)
        AS director_name, select_movies.movie_title
    FROM directors
         INNER JOIN 
        
            (SELECT filtered_movies.movie_title, movies_directors.director_id
                    FROM 
                        (SELECT movies.movie_id, movies.movie_title FROM movies
                             INNER JOIN 
                                movies_cast
                                ON movies_cast.movie_id = movies.movie_iD
                                WHERE movies_cast.role = 'SeanMaguire') as filtered_movies
                 INNER JOIN movies_directors
                ON movies_directors.movie_id = filtered_movies.movie_id) as select_movies
    ON select_movies.director_id = directors.director_id
    
