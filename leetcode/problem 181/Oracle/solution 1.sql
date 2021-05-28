-- Using INNER JOIN

SELECT Name AS "Employee"
FROM (
    SELECT Emp1.Name AS Name, Emp1.Salary AS Salary, Emp2.Salary AS ManagerSalary
    FROM Employee Emp1
    INNER JOIN Employee Emp2
    ON Emp1.ManagerId = Emp2.Id
    )  
WHERE Salary > ManagerSalary;
