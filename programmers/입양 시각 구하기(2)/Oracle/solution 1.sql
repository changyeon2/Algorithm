SELECT 
    "HOUR",
    SUM("COUNT") AS "COUNT"
FROM(
    (SELECT
        TO_NUMBER(TO_CHAR(DATETIME,'HH24')) AS "HOUR",
        COUNT(*) AS "COUNT"
    FROM
        ANIMAL_OUTS   
    GROUP BY
        TO_NUMBER(TO_CHAR(DATETIME ,'HH24')))
    UNION
    (SELECT 
        LEVEL-1,
        0
    FROM 
        DUAL
    CONNECT BY 
        LEVEL <= 24)
)
GROUP BY 
    "HOUR"
ORDER BY
    "HOUR";
