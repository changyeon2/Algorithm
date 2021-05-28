SELECT Name as Customers
FROM(
    SELECT Customers.Id, Name, CustomerId
    FROM Customers
    LEFT JOIN Orders
    ON Customers.Id = Orders.CustomerId
    GROUP BY Customers.Id, Name, CustomerId
    HAVING CustomerId IS NULL;
    )
