--using Dynamic SQL & DENSE_RANK()

CREATE FUNCTION getNthHighestSalary(N IN NUMBER) RETURN NUMBER IS
result NUMBER;
query VARCHAR2(1000);
BEGIN
    query := 'SELECT (
                      SELECT DISTINCT Salary
                      FROM (
                            SELECT Salary, DENSE_RANK() OVER (ORDER BY Salary DESC) as rank
                            FROM Employee
                           )
                      WHERE rank = ' || N || '
                     ) AS "getNthHighestSalary(' || N || ')" 
              FROM DUAL';
    
    EXECUTE IMMEDIATE query INTO result;
    
    RETURN result;
END;
