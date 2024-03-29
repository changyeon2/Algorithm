SELECT
    ANIMAL_ID,
    NAME
FROM(
    SELECT
        ANIMAL_INS.ANIMAL_ID,
        ANIMAL_INS.NAME,
        ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME AS "DIFF"
    FROM(
        ANIMAL_INS INNER JOIN ANIMAL_OUTS
        ON ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
    )
    ORDER BY
        "DIFF" DESC
)
WHERE
    ROWNUM = 1 
    OR ROWNUM = 2;
