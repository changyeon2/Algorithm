SELECT 
    Department.Name as "Department",
    Employee.Name as "Employee",
    Salary as "Salary"
FROM 
(   
    Employee
        INNER JOIN 
    Department ON Employee.DepartmentId = Department.Id
)
WHERE 
(DepartmentId, Salary) IN
(
    SELECT DepartmentId, MAX(Salary)
    FROM Employee
    GROUP BY DepartmentId
);
