-- FROM DUAL 하는 이유는, return 값이 NO ROWS일 때, NULL을 return하기 위함!

SELECT (
    SELECT DISTINCT Salary
    FROM (
        SELECT Salary, RANK() OVER (ORDER BY Salary DESC) as rank
        FROM Employee
        )
    WHERE rank = 2;
    ) AS "SecondHighestSalary"
FROM DUAL;
