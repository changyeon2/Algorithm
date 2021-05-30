-- Using INNER JOIN twice
SELECT
    Request_at AS "Day",
    ROUND(SUM(CASE WHEN Status != 'completed' THEN 1 ELSE 0 END) / COUNT(*), 2) AS "Cancellation Rate"
FROM(
    SELECT 
        Status,
        Request_at
    FROM
        Trips
        INNER JOIN Users User1 ON Trips.Client_Id = User1.Users_Id
        INNER JOIN Users User2 ON Trips.Driver_Id = User2.Users_Id   
    WHERE
        User1.Banned = 'No'
        AND User2.Banned = 'No'
        AND Request_at BETWEEN '2013-10-01' AND '2013-10-03'
)
GROUP BY Request_at;
