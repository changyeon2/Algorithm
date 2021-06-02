-- Using CASE WHEN ~ THEN ~ ELSE ~ END

SELECT
    id AS "id",
    CASE WHEN MOD(id, 2) = 0
    THEN LAG(student) OVER(ORDER BY id)
    ELSE(
        CASE WHEN LEAD(student) OVER(ORDER BY id) IS NULL
        THEN student
        ELSE LEAD(student) OVER(ORDER BY id)
        END
        )
    END AS "student"
FROM
    seat
ORDER BY
    "id";
