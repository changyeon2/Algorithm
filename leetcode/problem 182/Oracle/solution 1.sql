-- Using GROUP BY ~ HAVING, COUNT()

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(Email) >= 2;
