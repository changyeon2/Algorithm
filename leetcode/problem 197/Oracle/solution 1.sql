SELECT 
    id
FROM(
    SELECT
        id,
        recordDate - LAG(recordDate) OVER(ORDER BY recordDate) AS DateDiff,
        LAG(Temperature) OVER(ORDER BY recordDate) as YesterdayTemp,
        Temperature as TodayTemp
    FROM 
        Weather
)
WHERE 
    YesterdayTemp < TodayTemp
    AND DateDiff = 1;
