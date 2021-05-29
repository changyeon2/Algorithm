SELECT
    Department.Name AS "Department",
    RankedEmployee.Name AS "Employee",
    RankedEmployee.Salary AS "Salary"    
FROM(
    SELECT
        Employee.*,
        DENSE_RANK() OVER(
            PARTITION BY Employee.DepartmentId
            ORDER BY Salary DESC
            ) AS Rank
    FROM 
        Employee
    ) RankedEmployee
INNER JOIN Department ON RankedEmployee.DepartmentId = Department.Id
WHERE Rank BETWEEN 1 AND 3;
