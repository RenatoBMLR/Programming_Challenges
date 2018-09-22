SELECT reviewers.reviewer_name 
    FROM reviewers
    INNER JOIN ratings
    ON reviewers.reviewer_id = ratings.reviewer_id
    WHERE ratings.reviewer_stars IS NULL
