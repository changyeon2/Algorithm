SELECT Score as "score", DENSE_RANK() OVER (ORDER BY Score DESC) as "Rank"
FROM Scores;
