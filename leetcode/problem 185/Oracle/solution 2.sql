SELECT
    Department.Name AS "Department",
    Emp1.Name AS "Employee",
    Emp1.Salary AS "Salary"    
FROM Employee Emp1
INNER JOIN Department ON Emp1.DepartmentId = Department.Id
WHERE
    /* 1등은 자기보다 큰 애가 0, 2등은 1, 3등은 2개일 것이므로! */
    3 > (SELECT 
            COUNT(DISTINCT Emp2.Salary) /* 자기보다 큰 Salary의 종류?, 즉, DISTINCT한 것들의 개수를 알아야 함! (같은 값이 여러 개 있을 수 있다) */
        FROM
            Employee Emp2
        WHERE
            Emp1.Salary < Emp2.Salary
            AND Emp1.DepartmentId = Emp2.DepartmentId
        );
