SELECT *    
FROM(
    SELECT
        NAME,
        COUNT(*) AS COUNT
    FROM
        ANIMAL_INS
    WHERE
        NAME IS NOT NULL
    GROUP BY
        NAME
    ORDER BY
        NAME
    )
WHERE
    COUNT >= 2;
