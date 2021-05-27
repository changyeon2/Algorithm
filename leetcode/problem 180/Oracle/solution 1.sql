SELECT DISTINCT NUM as "ConsecutiveNums"
FROM(
    SELECT LAG(NUM) OVER(ORDER BY Id) AS Before, NUM, LEAD(NUM) OVER(ORDER BY Id) AS After
    FROM Logs
)
WHERE Before = NUM AND After = NUM;
