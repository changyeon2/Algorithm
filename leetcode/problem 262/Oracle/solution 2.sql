-- Solution without join

WITH NotBanned AS (
    SELECT
        Users_Id
    FROM 
        Users
    WHERE Banned = 'No'
)
SELECT 
    Request_at AS "Day",
    ROUND(SUM(CASE WHEN Status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS "Cancellation Rate"
FROM 
    Trips
WHERE
    Request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND Client_id IN (SELECT * FROM NotBanned)
    AND Driver_id IN (SELECT * FROM NotBanned)
GROUP BY 
    Request_at;
