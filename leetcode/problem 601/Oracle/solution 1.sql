SELECT
    id AS "id",
    TO_CHAR(visit_date, 'YYYY-MM-DD') AS "visit_date",
    people AS "people"
FROM(
    SELECT
        Filtered.*,
        LAG(id, 1) OVER(ORDER BY id) AS OneDayBefore,
        LAG(id, 2) OVER(ORDER BY id) AS TwoDaysBefore,
        LEAD(id, 1) OVER(ORDER BY id) AS OneDayAfter,
        LEAD(id, 2) OVER(ORDER BY id) AS TwoDaysAfter
    FROM(
        SELECT 
            *
        FROM 
            Stadium
        WHERE
            people >= 100
        ) Filtered
    )
WHERE
    (OneDayAfter = id + 1 AND TwoDaysAfter = id + 2)
    OR (OneDayBefore = id - 1 AND OneDayAfter = id + 1)
    OR (OneDayBefore = id - 1 AND TwoDaysBefore = id - 2);
